
import os
import PyPDF2
import uuid
import json
import hashlib
import shutil
import requests
import pandas as pd
from datetime import datetime
from urllib.parse import urlparse
from scrapy.http import HtmlResponse  # type: ignore
from multiprocessing import Pool
from pathlib import Path
import time
import mysql.connector
import re

# Configuration
OEM = "fls"
url_table = OEM
FILES_DIR = Path(f"./{OEM}/files")
FILES_INDEX_PATH = Path(f"./{OEM}/files.json")
FILES_DIR.mkdir(parents=True, exist_ok=True)

def remove_whitespace(text):
    symbols_to_replace = ['™', '®', '©', '*', '•', '\xa0', '\n', '\u00b0', '\\u', '\u00d7']
    try:
        cleantext = re.sub(r"[\t\n\s]+", " ", text)
    except:
        cleantext = text
    if isinstance(cleantext, str):
        cleantext = cleantext.strip()
        while cleantext.startswith(' ') or cleantext.startswith('|'):
            cleantext = cleantext[1:]
        while "||" in cleantext or "| |" in cleantext:
            cleantext = cleantext.strip().replace('||', '|').replace('| |', '|').strip().strip(' |').strip()
        cleantext = cleantext.rstrip('| ').lstrip('| ')
        for symbol in symbols_to_replace:
            cleantext = re.sub(re.escape(symbol), '', cleantext)
    return cleantext


def safe_name(name):
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    return name.strip().strip('.')


def database_connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Actowiz",
            database="oem_fls"
        )
        return conn
    except mysql.connector.Error as err:
        print("❌ Database connection Error:", err)
        return False


headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()



def download_and_index_file(url, path, files_index, max_retries=5):
    if pd.isna(url):
        print("⚠️ URL is empty/NaN. Skipping...")
        return None

    # 🎥 Skip embedded videos
    if "video.flsmidth.com" in url:
        print(f"🎥 Video URL detected (not downloadable): {url}")
        return {
            "file_uuid": None,
            "file_type": "video_url",
            "file_size_bytes": None,
            "creation_date": None,
            "video_url": url
        }

    attempt = 0
    while attempt < max_retries:
        try:
            print(f"⬇️ Downloading: {url}")
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            original_name = os.path.basename(urlparse(url).path)
            extension = Path(original_name).suffix
            if not extension:
                content_type = response.headers.get('Content-Type', '')
                if '/' in content_type:
                    mime_subtype = content_type.split('/')[-1].split(';')[0]
                    extension = f".{mime_subtype}"

            temp_path = path / f"temp_{original_name}"
            with open(temp_path, "wb") as f:
                f.write(response.content)

            file_hash = calculate_file_hash(temp_path)
            for entry in files_index["files"]:
                if entry["file_hash"] == file_hash:
                    print("⚠️ Duplicate file found. Skipping download.")
                    temp_path.unlink()
                    return entry.get("file_uuid") + extension, None, None, None  # Use existing UUID

            file_uuid = f"{uuid.uuid4()}{extension}"
            stored_path = path / file_uuid
            shutil.move(temp_path, stored_path)

            # Append minimal info to files_index
            files_index["files"].append({
                "file_name": "image" if "image" in url.lower() else "download",
                "file_hash": file_hash,
                "file_uuid": file_uuid.split('.')[0],  # store UUID without extension
                "original_url": url,
                "extraction_time": datetime.utcnow().isoformat(),
                "file_size_bytes": os.path.getsize(stored_path)
            })

            print(f"✅ Saved to: {stored_path}")
            return file_uuid, extension.replace(".", ""), os.path.getsize(stored_path), response.headers.get("Last-Modified") or None

        except Exception as e:
            attempt += 1
            print(f"[Retry {attempt}/{max_retries}] ❌ Error downloading {url}: {e}")
            time.sleep(1)

    return None



def get_data(row, all_files_index):
    try:
        files_index = {"files": []}

        # 🛡️ Safe model_id
        model_id = safe_name(remove_whitespace(str(row.get("model_id", ""))))
        if not model_id:
            print("❌ Skipping row due to missing model_id")
            return

        # 🛡️ Safe categories
        try:
            categories = json.loads(row.get("categories", "[]"))
        except Exception as e:
            print(f"❌ Error parsing categories for {model_id}: {e}")
            return

        if len(categories) < 3:
            print(f"⚠️ Skipping due to insufficient categories: {categories}")
            return

        main_category = safe_name(remove_whitespace(categories[1]))
        main_category = main_category.replace(" ", "_")
        print('main_category', main_category)
        # if main_category.lower() != "classification":
        #     return  # only create folders for classification

        sub_category = safe_name(remove_whitespace(categories[2]))
        sub_category = sub_category.replace(" ", "_")
        print('sub_category', sub_category)


        model_id_folder = model_id.replace(" ", "_")
        print('model_id_folder', model_id_folder)

        # 🛠️ Create directories
        product_dir = Path(f"./{OEM}/{main_category}/{sub_category}/{model_id_folder}")
        print(f"product_dir: {product_dir}")

        # product_dir=product_dir.

        product_dir.mkdir(parents=True, exist_ok=True)
        image_path = product_dir / "image"
        image_path.mkdir(parents=True, exist_ok=True)

        print(f"\n📦 Processing: model_id_folder")

        # ✅ Parse all media fields
        def try_json(field):
            try:
                return json.loads(row.get(field, "[]"))
            except Exception:
                return []

        attachments = try_json("attachments")

        attachment_img_link=attachments[0].get('main_image_url'," ")
        attachment_video_link = attachments[0].get('main_video_url', " ")
        print('attachment_img_link', attachment_img_link)
        print('attachment_video_link', attachment_video_link)
        manuals = try_json("manuals")
        print('manuals', manuals)

        manual_links = [manual.get('url', '') for manual in manuals]
        print('manual_links:', manual_links)

        images = try_json("images")
        print("images",images)

        img_link=images[0].get("url"," ")
        print('img_link',img_link)


        bom = try_json("bom")
        metadata = try_json("metadata")
        technical_specs = try_json("technical_specs")
        secondary_identifiers = try_json("secondary_identifiers")
        manufacturer = try_json("manufacturer")
        print(manufacturer)
        print('/////////////')


        # 🔽 Download function
        def download_files(file_list, folder,section=None):
            downloaded = []
            #########################################################
            for f in file_list:
                print('f',f)
                urls = []
                if f.get("url"):
                    print('f.get("url")',f.get("url"))
                    urls.append(f.get("url"))
                if f.get("main_image_url"):
                    print('f.get("main_image_url")',f.get("main_image_url"))
                    urls.append(f.get("main_image_url"))
                if f.get("main_video_url"):
                    print('f.get("main_video_url")',f.get("main_video_url"))
                    urls.append(f.get("main_video_url"))

                print('urls',urls)
                # exit(0)
                for url in urls:
                    # 🔽 Detect video URL and skip download
                    if "video.flsmidth.com" in url:
                        entry = {
                            "id": str(uuid.uuid4()),
                            "name": f.get("name", "") or None,
                            "description": f.get("description") or None,
                            "file_path": url,
                            "file_type": "video_url",
                            "file_size_bytes": file_size,
                            "creation_date": creation_date,
                            "metadata": {
                                "collected_at": metadata[0].get("collected_at", "") if isinstance(metadata,
                                                                                                  list) and metadata else "",
                                "data_source_url": attachment_video_link
                            }


                        }
                        downloaded.append(entry)
                        continue  # Skip actual download

                    result = download_and_index_file(url, folder, all_files_index)

                    if result:
                        uuid_file, file_type, file_size, creation_date = result

                        if folder == FILES_DIR:
                            file_path_local = os.path.join(FILES_DIR, uuid_file)
                        else:
                            file_path_local = os.path.join(
                                f"./{OEM}/{main_category}/{sub_category}/{model_id_folder}/image",
                                uuid_file
                            )

                            # 📄 Count pages if manual
                        page_count = None
                        if section == "manual" and uuid_file.endswith(".pdf"):
                            try:
                                with open(file_path_local, "rb") as pdf_file:
                                    reader = PyPDF2.PdfReader(pdf_file)
                                    page_count = len(reader.pages)
                            except Exception as e:
                                print(f"⚠️ Failed to read PDF page count: {e}")



                        if section =="manual":
                            entry={
                                "id": str(uuid.uuid4()),
                                "name": f.get("name", ""),
                                "description":None,
                                "manufacturer":None,
                                "file_path": f"{OEM}/files/{uuid_file}" if folder == FILES_DIR else f"{OEM}/{main_category}/{sub_category}/{model_id_folder}/image/{uuid_file}",
                                "file_size_bytes": file_size,
                                "language": "en",
                                "publication_date":None,
                                "version":None,
                                "page_count":page_count,

                                "metadata": {
                                    "collected_at": metadata[0].get("collected_at", "") if isinstance(metadata,
                                                                                                      list) and metadata else "",
                                    "data_source_url": url
                                }

                            }



                        else:
                            # Determine correct source URL based on section or field origin

                            if section == "attachments":

                                if file_type == "video_url":
                                    data_source = f.get("main_video_url") or f.get("url")
                                    print('data_source',data_source)
                                else:
                                    data_source = f.get("main_image_url") or f.get("url")
                            else:
                                data_source = img_link

                            print('////////////////////////////////')

                            entry = {
                                "id": str(uuid.uuid4()),
                                "name": f.get("name", "") or None,
                                "description": f.get("description") or None,
                                "file_path": f"{OEM}/files/{uuid_file}" if folder == FILES_DIR else f"{OEM}/{main_category}/{sub_category}/{model_id_folder}/image/{uuid_file}",
                                "file_type": file_type,
                                "file_size_bytes": file_size,
                                "creation_date": creation_date,
                                "metadata": {
                                    "collected_at": metadata[0].get("collected_at", "") if isinstance(metadata,
                                                                                                      list) and metadata else "",
                                    "data_source_url": data_source
                                }
                            }



                        downloaded.append(entry)


            return downloaded

        downloaded_attachments = download_files(attachments, FILES_DIR)
        # 🧹 Remove PNG attachments
        downloaded_attachments = [
            att for att in downloaded_attachments
            if att.get("file_type") != "png" and not str(att.get("file_path", "")).lower().endswith(".png")
        ]


        # downloaded_attachments = [att for att in downloaded_attachments if att.get("file_type") != "png"]

        downloaded_manuals = download_files(manuals, FILES_DIR,section="manual")
        downloaded_images = download_files(images, image_path)
        print('/////////////////////////',downloaded_images)

        downloaded_bom = download_files(bom, FILES_DIR)

        import re

        name = str(row.get("name", "")).strip()
        cleaned_name = re.sub(r'\s+', ' ', name)  # Collapse multiple spaces to one

        # Remove special characters for id (keep only alphanumerics, spaces, and hyphens before replacing spaces)
        safe_for_id = re.sub(r'[^a-zA-Z0-9\s-]', '', cleaned_name)

        # Convert to lowercase, replace spaces with dashes, and collapse repeated dashes
        id_value = re.sub(r'-+', '-', safe_for_id.lower().replace(" ", "-"))



        data = {
            "id": id_value,
            "name": cleaned_name,
            "model_id": cleaned_name,  # Keep ™ symbol

            # "id": row.get("id",str(uuid.uuid4())),
            # "name": row.get("name", ""),
            # # "model_id": model_id,
            # "model_id": row.get("name", ""),  # match name field exactly
            "secondary_identifiers": secondary_identifiers,
            "manufacturer": manufacturer,
            "description": row.get("description", ""),
            "categories": categories,
            "short_description": row.get("short_description", ""),
            "technical_specs": technical_specs,
            "manuals": downloaded_manuals,
            # "images": downloaded_images,
            "images":[entry["file_path"] for entry in downloaded_images if "file_path" in entry],  # ✅ only file paths
            "attachments": downloaded_attachments,
            # "attachments": downloaded_attachments,
            "bom": downloaded_bom,

            "metadata": {
                "collected_at": metadata[0].get("collected_at", "") if isinstance(metadata, list) and metadata else "",
                "data_source_url": metadata[0].get("data_source_url", "") if isinstance(metadata,
                                                                                        list) and metadata else "",
                "scraper_version": None,
                "last_updated": None,
                "confidence_score": None,
                "processing_notes": None
            }


        }

        # ✅ Write to data.json
        with open(product_dir / "data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ data.json created for: {model_id}")



    except Exception as e:
        print(f"❌ General error for model_id {row.get('model_id', 'unknown')}: {e}")



def get_list(current_instances, total_instances):
    conn = database_connect()
    if not conn:
        print("❌ Database connection failed. Exiting get_list.")
        return []

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {url_table} WHERE scraped = '0' ORDER BY id")
    # cursor.execute(f"SELECT * FROM {url_table} WHERE scraped = '0' ORDER BY id LIMIT 1 OFFSET 18")
    row = cursor.fetchone()
    print(row)


    # cursor.execute(f"SELECT * FROM {url_table} WHERE scraped = '0' ORDER BY id")
    combo_list = cursor.fetchall()
    total_product_urls_no = len(combo_list)
    conn.close()

    print(f"📊 Total unscripted products: {total_product_urls_no}")
    top_index = (current_instances - 1) * int(total_product_urls_no / total_instances)
    end_index = top_index + int(total_product_urls_no / total_instances)
    return combo_list[top_index:end_index]


csv_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\OEM_final_csv_24.csv'
df = pd.read_csv(csv_path)

# # '''for classification category only
# def is_classification_category(row):
#     try:
#         categories = json.loads(row["categories"]) if row["categories"] else []
#         return len(categories) > 1 and categories[1].strip().lower() == "classification"
#     except Exception:
#         return False
#
# df = df[df.apply(is_classification_category, axis=1)]
# print(f"📦 Total Classification category products: {len(df)}")
# # '''



all_files_index = {"files": []}
for _, row in df.iterrows():
    get_data(row, all_files_index)

with open(FILES_INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(all_files_index, f, ensure_ascii=False, indent=2)




