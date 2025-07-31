import re
import json
import gzip
from urllib.parse import urljoin, urlparse, unquote, parse_qs

import requests
from parsel import Selector
from pprint import pprint
from datetime import datetime
import uuid
import os

# --- Setup ---
base_url = "https://fls.com"
equipment_url = "https://fls.com/en/equipment"

manufacturer_name = "FLS"
manufacturer_description = "N/A"
manufacturer_tags = "N/A"
manufacturer_founded_year = "N/A"
manufacturer_headquarters = "N/A"
founded_year = "N/A"

status = 'pending'
logo_url = 'https://cdn.brandfetch.io/idIvzS8s7W/w/400/h/400/theme/dark/icon.jpeg?c=1bxid64Mup7aczewSAYMX&t=1744768512866'
part_number = 'N/A'
identifiers1 = []
technical_specifications = []
features_and_benefits = []
parts = []

cookies = {
    'NEXT_LOCALE': 'en',
    'CookieConsent': '{stamp:%27CpifRPJjyfwHUku81D0vt2j1V02gCIHGQMsNiAGtUyhIVwgCYzTLzg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1749715525582%2Cregion:%27in%27}',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*',
}


def extract_real_image_url(image_url):
    if "_next/image" in image_url:
        parsed_url = urlparse(image_url)
        query = parse_qs(parsed_url.query)
        if "url" in query:
            return unquote(query["url"][0])
    return image_url


def get_filename_from_url(pdf_url):
    path = urlparse(pdf_url).path
    return path.split('/')[-2] if path else "No Label"


# --- Use specific product URLs ---

from urllib.parse import urlparse


def generate_breadcrumb(url):
    try:
        parts = urlparse(url).path.strip('/').split('/')
        if len(parts) >= 4:
            category = parts[2].replace('-', ' ').title()
            sub_category = parts[3].replace('-', ' ').title()
            return ["equipment", category, sub_category]
        return ["equipment"]
    except:
        return ["equipment"]


response = requests.get(equipment_url, cookies=cookies, headers=headers)

# url=response.url
# print(url)
print(response.status_code)

raw_html = response.text
# print(raw_html)

output_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\HTML_page\OEM_final_html_16.html'
gzip_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\HTML_page\OEM_final_gzip_16.html'

#
# with open(output_path, 'w', encoding='utf-8') as file:
#     file.write(raw_html)
# print("HTML content fetched and written successfully.")
#
# with open(output_path, 'rb') as file_binary:
#     with gzip.open(output_path + '.gz', 'wb') as file_gzip:
#         file_gzip.writelines(file_binary)
# print('file has been saved in compressed zip file.')

with open(output_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# selector = Selector(text=raw_html)
selector = Selector(text=html_content)

full_category_links = ['https://fls.com/en/equipment/grinding/high-pressure-grinding-rolls',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/slurry-pressure-pipe',
                       'https://fls.com/en/equipment/classification/hydrocyclones',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/dry-rotary-samplers',
                       'https://fls.com/en/equipment/crushing/cone-crushers',
                       'https://fls.com/en/equipment/flotation/column-flotation-cells',
                       'https://fls.com/en/equipment/flotation/forced-air-flotation-cells',
                       'https://fls.com/en/equipment/feeding-and-conveying/reclaim-feeders',
                       'https://fls.com/en/equipment/laboratory-equipment/metallurgical-testing',
                       'https://fls.com/en/equipment/classification/reflux-classifiers',
                       'https://fls.com/en/equipment/feeding-and-conveying/belt-feeders',
                       'https://fls.com/en/equipment/precious-metal-recovery/merrill-crowe-systems',
                       'https://fls.com/en/equipment/feeding-and-conveying/mine-hoists',
                       'https://fls.com/en/equipment/precious-metal-recovery/carbon-regeneration-kiln',
                       'https://fls.com/en/equipment/crushing/gyratory-crushers',
                       'https://fls.com/en/equipment/feeding-and-conveying/apron-feeders',
                       'https://fls.com/en/equipment/crushing/roll-crushers',
                       'https://fls.com/en/equipment/laboratory-equipment/size-determination',
                       'https://fls.com/en/equipment/grinding/vertical-fine-grinding-mills',
                       'https://fls.com/en/equipment/crushing/sizers',
                       'https://fls.com/en/equipment/feeding-and-conveying/hybrid-apron-feeders',
                       'https://fls.com/en/equipment/flotation/self-aspirated-flotation-cells',
                       'https://fls.com/en/equipment/pyroprocessing/gas-suspension-calciners',
                       'https://fls.com/en/equipment/pyroprocessing/high-temperature-shaft-kilns',
                       'https://fls.com/en/equipment/pyroprocessing/flash-dryers-and-heaters',
                       'https://fls.com/en/equipment/slurry-pumping/sump-pumps',
                       'https://fls.com/en/equipment/pyroprocessing/gear-drive-rotary-kilns',
                       'https://fls.com/en/equipment/filtration-and-dewatering/filters',
                       'https://fls.com/en/equipment/precious-metal-recovery/cyanide-leach',
                       'https://fls.com/en/equipment/slurry-pumping/mill-pumps',
                       'https://fls.com/en/equipment/slurry-pumping/valves',
                       'https://fls.com/en/equipment/slurry-pumping/froth-pumps',
                       'https://fls.com/en/equipment/slurry-pumping/large-solids-pumps',
                       'https://fls.com/en/equipment/classification/heavy-media-hydrocyclones',
                       'https://fls.com/en/equipment/laboratory-equipment/thermogravimetric-analysis',
                       'https://fls.com/en/equipment/grinding/ball-mills',
                       'https://fls.com/en/equipment/crushing/crushing-stations',
                       'https://fls.com/en/equipment/laboratory-equipment/dividing',
                       'https://fls.com/en/equipment/laboratory-equipment/drying',
                       'https://fls.com/en/equipment/slurry-pumping/high-pressure-pumps',
                       'https://fls.com/en/equipment/slurry-pumping/recessed-impeller-pumps',
                       'https://fls.com/en/equipment/feeding-and-conveying/conveyors',
                       'https://fls.com/en/equipment/flotation/mixed-flotation-cells',
                       'https://fls.com/en/equipment/flotation/attrition-scrubbers',
                       'https://fls.com/en/equipment/precious-metal-recovery/Mercury-retort-and-abatement-systems',
                       'https://fls.com/en/equipment/classification/desander-hydrocyclones',
                       'https://fls.com/en/equipment/slurry-pumping/medium-duty-pumps',
                       'https://fls.com/en/equipment/slurry-pumping/split-case-pumps',
                       'https://fls.com/en/equipment/feeding-and-conveying/vibrating-feeders',
                       'https://fls.com/en/equipment/slurry-pumping/heavy-duty-process-pumps',
                       'https://fls.com/en/equipment/laboratory-equipment/automated-laboratories',
                       'https://fls.com/en/equipment/precious-metal-recovery/Precious-metals-refinery',
                       'https://fls.com/en/equipment/grinding/sag-and-ag-mills',
                       'https://fls.com/en/equipment/laboratory-equipment/Crushing',
                       'https://fls.com/en/equipment/flotation/coarse-flotation-cells',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/slurry-gravity',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/sample-collectors',
                       'https://fls.com/en/equipment/crushing/jaw-crushers',
                       'https://fls.com/en/equipment/pyroprocessing/multiple-hearth-furnace',
                       'https://fls.com/en/equipment/precious-metal-recovery/gravity-concentration',
                       'https://fls.com/en/equipment/precious-metal-recovery/carbon-adr-plants',
                       'https://fls.com/en/equipment/precious-metal-recovery/Precious-metals-electrowinning',
                       'https://fls.com/en/equipment/filtration-and-dewatering/centrifuges',
                       'https://fls.com/en/equipment/flotation/reflux-flotation-cell',
                       'https://fls.com/en/equipment/pyroprocessing/rotary-dryers',
                       'https://fls.com/en/equipment/feeding-and-conveying/mineshaft',
                       'https://fls.com/en/equipment/laboratory-equipment/pulverising',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/online-analysis',
                       'https://fls.com/en/equipment/sampling-and-online-analysis/dry-linear-samplers',
                       'https://fls.com/en/equipment/filtration-and-dewatering/thickeners-and-clarifiers',
                       'https://fls.com/en/equipment/pyroprocessing/indirectly-heated-rotary-kilns']

print(len(full_category_links))
# # print(full_category_links)
#
remove_links = ['https://fls.com/en/equipment/pyroprocessing/gas-suspension-calciners',
                'https://fls.com/en/equipment/precious-metal-recovery/gravity-concentration',
                'https://fls.com/en/equipment/feeding-and-conveying/conveyors',
                'https://fls.com/en/equipment/feeding-and-conveying/hybrid-apron-feeders',
                'https://fls.com/en/equipment/crushing/roll-crushers']

full_category_links = [link for link in full_category_links if link not in remove_links]
print(len(full_category_links))
# exit(0)


# full_category_links = [
# # 'https://fls.com/en/equipment/grinding/high-pressure-grinding-rolls'
# 'https://fls.com/en/equipment/classification/reflux-classifiers'
# ]

final_data = []
# id=1
product_counter = 1
for product in full_category_links:
    print(f"\n🔍 Processing: {product}")
    filepath = fr"C:\Users\Madri.Gadani\Desktop\madri\OCM\HTML_page\product_pages"

    # Get the last part of the URL to use as filename
    page_name = product.rstrip('/').split('/')[-1] + '.html'
    full_path = os.path.join(filepath, page_name)

    if os.path.exists(full_path):
        print(f"✅ Reading from saved file: {page_name}")
        with open(full_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    else:
        print(f"🌐 Sending request to fetch: {product}")
        response = requests.get(product)
        html_content = response.text

    # response = requests.get(product, cookies=cookies, headers=headers)
    # response.encoding = 'utf-8'
    # selector = Selector(text=response.text)
    selector = Selector(text=html_content)
    main_item = {
        'product_url': product,
        'website_url': equipment_url,
        'manufacturer_name': manufacturer_name,
        'manufacturer_description': manufacturer_description,
        'manufacturer_tags': manufacturer_tags,
        'manufacturer_founded_year': manufacturer_founded_year,
        'manufacturer_headquarters': manufacturer_headquarters,
        'logo_url': logo_url,
        'status': status,
        'part_number': part_number,
        'founded_year': founded_year,

    }

    # --- Image ---
    img = selector.xpath('//div[@class="relative aspect-square"]//@src').get()
    main_item['image_url'] = extract_real_image_url(urljoin(base_url, img)) if img else None

    video = selector.xpath('//div[@class="relative w-full aspect-video"]/iframe/@src').getall()
    main_item['video_url'] = video[0] if video else None

    title1 = selector.xpath(
        '//div[@class="flex gap-2 items-center text-sm @md:text-base font-medium before:w-2.5 before:h-2.5 before:rounded-full before:bg-blue-electric"]/text()').getall()
    # print(title1)
    title = selector.xpath('//div[@class="min-h-full flex flex-col gap-12"]//h1/text()').getall()
    # print(title) #['Pump the most abrasive grinding mill slurries ']
    desc = selector.xpath('//div[@class="min-h-full flex flex-col gap-12"]//p/text()').getall()
    main_item['main_title'] = title1[0] + '-' + ' '.join(title).strip() if title else None

    cleaned_desc = ' '.join(d.strip() for d in desc if d.strip())
    main_item['main_short_description'] = cleaned_desc if cleaned_desc else None

    pdp_variation_list = []
    for i in selector.xpath("//h3[contains(@class, 'font-medium') and contains(@class, 'text-balanc')]"):
        temp_dict = {}
        temp_dict["model_name"] = ' '.join(i.xpath(".//text()").getall()).strip()
        temp_dict["model_short_desc"] = ''.join(i.xpath(".//following-sibling::div//text()").getall()).strip()

        container = i.xpath("./ancestor::div[contains(@class, 'flex') or contains(@class, 'gap')]")[1]
        model_img_url = container.xpath(".//img/@src").get()
        temp_dict["model_img_url"] = urljoin(base_url, model_img_url) if model_img_url else None

        video_url1 = container.xpath('//div[@class="pt-2"]/a/@href').getall()
        model_video_url1 = [vurl for vurl in video_url1 if "video.flsmidth.com" in vurl]
        model_video_url = model_video_url1 if model_video_url1 else None
        # print(model_video_url)
        temp_dict["model_video_url"] = model_video_url if model_video_url else None
        pdp_variation_list.append(temp_dict)

    main_item['pdp_variation_list'] = pdp_variation_list if pdp_variation_list else None

    # --- Technical Details ---

    main_description = []

    for specs in selector.xpath(
            "//div[contains(@class, 'accordion-slide-transition')]"):
        temp_dict = dict()
        heading = specs.xpath('.//h3//text()').get()
        if "?" in heading:
            continue
        temp_dict['key'] = heading.strip()
        paragraphs = specs.xpath('.//p//text() | .//li//text() | .//text()[not(ancestor::h3)]').getall()

        cleaned_text = re.sub(r'\s+', ' ', ' '.join(t.strip() for t in paragraphs if t.strip()))
        temp_dict['value'] = cleaned_text if cleaned_text else "N/A"

        main_description.append(temp_dict)
    main_item['main_description'] = main_description if main_description else []  #

    # --- PDFs ---
    pdf_lst = []
    pdf_link = selector.xpath('//ul[contains(@class,"grid") and contains(@class,"border-grey-metal")]//li')
    if not pdf_link:
        pdf_link = selector.xpath('//ul[contains(@class,"grid")]//li')

    for pdf in pdf_link:
        link = pdf.xpath('.//a/@href').get()
        raw_text = pdf.xpath('.//text()').getall()
        cleaned_text = ' '.join(t.strip() for t in raw_text if t.strip())

        if link:
            pdf_dict = {
                'name': cleaned_text if cleaned_text else get_filename_from_url(link),
                'url': urljoin(base_url, link)
            }

            pdf_lst.append(pdf_dict)

    # --- Remove Duplicates ---
    seen = set()
    unique_pdf_lst = []
    for item in pdf_lst:
        if item['url'] not in seen:
            unique_pdf_lst.append(item)
            seen.add(item['url'])

    # --- Create final flattened list ---

    for model in pdp_variation_list:
        flattened_entry = {
            # 'id': model["model_name"].lower().replace(" ", "-"),
            'id': re.sub(r"[®™]", "", model["model_name"]).lower().replace(" ", "-"),
            # 'part_number':main_item['part_number'],
            "name": model["model_name"],
            "model_id": model["model_name"],
            # "url": main_item["product_url"],
            "secondary_identifiers": identifiers1,
            "manufacturer": [{
                "name": main_item["manufacturer_name"],
                "description": main_item["manufacturer_description"],
                "website": main_item["website_url"],
                "logo_url": main_item["logo_url"],
                "tags": main_item["manufacturer_tags"],
                "founded_year": main_item["founded_year"],
                "headquarters": main_item["manufacturer_headquarters"],
            }],

            "description": "\n".join([
                f" {model["model_short_desc"]}",
                *[
                    f"  - {d['key']}: {d['value']}"

                    for d in main_item.get("main_description", [])
                ]
            ]),

            "categories": generate_breadcrumb(main_item["product_url"]),

            "short_description": "\n".join([
                f"{main_item['main_title']}:",
                f" {main_item['main_short_description']}"]),

            "technical_specs": technical_specifications,

            # "features_and_benefits":features_and_benefits,

            "manuals": unique_pdf_lst if unique_pdf_lst else [],
            # "manuals": [{"pdf_url": unique_pdf_lst if unique_pdf_lst else None}],
            "images": [{
                "name": model["model_name"],
                "url": model["model_img_url"]

            }],
            "attachments": [{
                'id': model["model_name"].lower().replace(" ", "-"),
                "name": model["model_name"],
                "url": model["model_video_url"] if model["model_video_url"] else 'N/A',
                "main_image_url": main_item["image_url"] if main_item["image_url"] else 'N/A',
                "main_video_url": main_item["video_url"] if main_item["video_url"] else 'N/A',
                # "pdf_url":unique_pdf_lst if unique_pdf_lst else None,
            }],
            # "parts": parts,
            "metadata": [
                {
                    "collected_at": datetime.now().isoformat(),
                    "data_source_url": main_item["product_url"],
                    "scraper_version":None,
                    "last_updated":None,
                    "confidence_score":None,
                    "processing_notes":None


                }]

        }

        final_data.append(flattened_entry)
        product_counter += 1
        # id +=1

        # --- Preview Output (Optional for debugging) ---
    if final_data:
        pprint(final_data[-1])  # Only last model printed
    else:
        print("⚠️ No product model data was found for this page.")

    # pprint(final_data[-1])  # Only last model printed
    print("\n✅ Finished: ", product)
    print('----------------------------------------------------------')

import json
import csv

# --- Your paths ---
json_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\OEM_final_json_24.json'
csv_path = r'C:\Users\Madri.Gadani\Desktop\madri\OCM\OEM_final_csv_24.csv'


# --- Function to clean symbols ---
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = text.strip()
    if text.upper() == 'N/A':
        return None
    try:
        text = text.encode('latin1').decode('utf-8')
    except UnicodeEncodeError:
        pass
    except UnicodeDecodeError:
        pass

    # Replace known problematic sequences as fallback
    return (
        text.replace("â€“", "-")
        .replace("â€”", "--")
        .replace("â€˜", "'")
        .replace("â€™", "'")
        .replace("â€œ", '"')
        .replace("â€�", '"')
        .replace("â€¦", "...")
        .replace("Â", "")
    )


def clean_nested(data):
    if isinstance(data, dict):
        return {k: clean_nested(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_nested(v) for v in data]
    elif isinstance(data, str):
        return clean_text(data)
    else:
        return data


cleaned_data = clean_nested(final_data)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

print("✅ JSON saved after full cleaning.")

# --- Define your fieldnames ---
fieldnames = [
    "id",
    # "part_number",
    "name",
    "model_id",
    # "url",
    "secondary_identifiers",
    "manufacturer",
    "description",
    "categories",
    "short_description",
    "technical_specs",
    # "features_and_benefits",
    "manuals",
    "images",
    "attachments",
    # "parts",
    "metadata"
    # "status"
]

# --- Write cleaned data to CSV ---
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for item in cleaned_data:  # ✅ Use cleaned_data here
        row = {}
        for field in fieldnames:
            value = item.get(field, "null")

            if isinstance(value, (list, dict)):
                value = json.dumps(value, ensure_ascii=False)

            row[field] = value

        writer.writerow(row)

print(f"✅ Cleaned CSV saved at: {csv_path}")




















