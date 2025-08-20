import requests
from parsel import Selector
import gzip
import mysql.connector
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Global headers and cookies
cookies = {
    'Network-Type': '4g',
    'T': 'TI174824499597300142754598348542330031370306090257579454047282066136',
    'vw': '1366',
    'dpr': '1',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20305%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754896184%7C12%7CMCAAMB-1754896184%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754298584s%7CNONE%7CMCAID%7CNONE',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwNDEzMDY0MTM0NlhZMVFQQjQiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDA3MzAwMSwiaWF0IjoxNzU0MjkzMDAxLCJqdGkiOiJmNjkxNjlkMS1iZjQ4LTQyYmUtYTZmNy02YTQwMjNkZDJhYTUifQ.SKmnWwLkb78ePUma4KSDEwCPfi3poN8hGsdKbBCJDaU',
    'ud': '1.3RovXtHZlV6Ku4MnxYAGp12z9rswmi-Rm7GUyv5aizXCUI2_V6rn93V7V4ogfQ4fm36i3_Z-aKTDlXSoF8wff_IQZNwjcoc8StHK3heQPEGKiQ7fD2YXEJAqNIjdvPbYIcP0uyVQK_Y7JMx2MsbJpX0PzkH-h809MqE7h0TzhCgNLPAU3b7cXPjoKOGrtttm',
    'qH': '3a4bc565a4835306',
    'vh': '607',
    'K-ACTION': 'null',
    'Network-Type': '4g',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aclothing-and-accessories%25253Asaree-and-accessories%25253Asaree%25253Awomen-saree%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLABEL',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NTQzOTgwODYsImlhdCI6MTc1NDM5NjI4NiwiaXNzIjoia2V2bGFyIiwianRpIjoiNzgxMWI4NDMtM2E0My00ODc5LThlOTctZTA0YzVkM2U0YWFjIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJOUENDSU4iLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6Ikh1dnp3VVJfMjNfMEVWaEdZVzFudzVlblptUG9DZ2pzaURXcE5iSGpqeFpoZWpBZGNRUm9wZz09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YaY9t4-OlWKS9ZN8BtWgFO1ssH97B0ANI7aYxD1kLQ8',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzAyOTM4ODYsImlhdCI6MTc1NDM5NjI4NiwiaXNzIjoia2V2bGFyIiwianRpIjoiY2Y2MzE2YWQtZDE2Yy00NWYzLWFlM2EtNTAzNDBmNjMxY2IzIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJOUENDSU4iLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiUkg0QzJFIn0.1LwkTCgg0xnEzp62754Ou8LhMInCGtKhzPeEXaqF8LA',
    'S': 'd1t16Pz8/cz97Pwk/Pz8/PzRHP0yCWGrNF/yaaYkSbMiPDJQ9EEX37c4ffSMcEeC70phHEgCX+bg90yYET3VrOBMh1g==',
    'vd': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872-1754284011313-7.1754396726.1754391734.158529491',
    'SN': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK37FC9F697D514E74885B72C818ADD1EF.1754396742543.LI',
}


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version': '"138.0.7204.158"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.158", "Google Chrome";v="138.0.7204.158"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    # 'Cookie': 'Network-Type=4g; T=TI174824499597300142754598348542330031370306090257579454047282066136; rt=null; K-ACTION=null; ud=7._EA8MPay8RgQCnXpsBXZHDhEvrPi_FigMKvNKmSmvPkYNsXpjGM3sYBdoc3UdkrlNyE0WjSJs9YHBeCXrvRRnRlm3F8DwKy2yKyTzWwt15btu3Dh9NCHLAZB5HSBDMKK9HnDy5_h6L6yK5COVaD2Aw; vw=1366; dpr=1; vh=641; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3NTU0MTI4ODAsImlhdCI6MTc1MzY4NDg4MCwiaXNzIjoia2V2bGFyIiwianRpIjoiMTBmODRlN2MtYjYwZC00NTQxLTgzYjAtNGQ4MTc2YWQyODYzIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.uRkVBGj_YPFHtMKQyqsrWf5wigFoikhZTAV7iCMaCvs; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; Network-Type=4g; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20302%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754289652%7C12%7CMCAAMB-1754622877%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754025277s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; vd=VI5FAAFE7DD4B443C198E5E65ACCA7C872-1748244997568-25.1754020985.1754017754.163439705; S=d1t16Pz9MTj99Pz9PPz8fST8EP+ZO54wrqFnBw3mVTQCDooFGHj1V8d2pOFcOKwttS5AMtjbVJn26GLESZCo9m7jLjA==; SN=VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOKDB4F35E4133A4C6084AACB725B67E80F.1754020985965.LO',
}

sort_by_list = ['price_asc', 'price_desc', 'recency_desc', 'popularity']
html_dir = r'D:\flipkart\flipkart_saree_html'
os.makedirs(html_dir, exist_ok=True)

def process_filter(filter_row):
    # Open new DB connection per thread
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Actowiz',
        database='flipkart_saree'
    )
    cursor = conn.cursor(dictionary=True)

    filter_id = filter_row['id']
    url = filter_row['url']
    filter_name = filter_row['filter_name']
    filter_type = filter_row['filter_type']

    try:
        response = requests.get(url, cookies=cookies, headers=headers)
        print(f"[{filter_name}] Status: {response.status_code}")

        if response.status_code != 200:
            raise Exception("Failed to fetch initial page")

        selector = Selector(text=response.text)
        visible_site_count = selector.xpath('.//span[@class="BT4kdg"]//text()').get()
        product_count = visible_site_count.split(' ')[-2] if visible_site_count else "0"
        product_count = int(product_count.replace(',', ''))

        page_urls = (
            [(f"{url}&sort={sort}&page=0", sort) for sort in sort_by_list]
            if product_count > 1000 else [(f"{url}&page=0", None)]
        )

        for page_url, sort in page_urls:
            for page_num in range(1, 26):
                paginated_url = f"{page_url.split('&page=')[0]}&page={page_num}"
                print(f"[{filter_name}] Requesting Page {page_num}: {paginated_url}")
                res = requests.get(paginated_url, cookies=cookies, headers=headers)

                if res.status_code != 200:
                    print(f"[{filter_name}] Failed to fetch page {page_num}, skipping.")
                    continue

                raw_html = res.text
                sort_suffix = f"_{sort}" if sort else ""
                safe_filter_name = filter_name.replace(" ", "_")
                filename = f"saree_{safe_filter_name}{sort_suffix}_page{page_num}.html"
                html_path = os.path.join(html_dir, filename)

                # Save HTML
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(raw_html)
                with open(html_path, 'rb') as fb:
                    with gzip.open(html_path + '.gz', 'wb') as fg:
                        fg.writelines(fb)

                selector = Selector(text=raw_html)
                products = selector.xpath('//div[@class="_1sdMkc LFEi7Z"]')
                for item in products:
                    relative_link = item.xpath('.//a/@href').get()
                    print('relative_link.................',relative_link)
                    if not relative_link:
                        continue
                    full_link = 'https://www.flipkart.com' + relative_link
                    print('full_link-------------------',full_link)
                    PID = relative_link.split("?pid=")[-1].split("&")[0].strip()


                    try:
                        cursor.execute('''
                            INSERT INTO product_links 
                            (product_link, filter_name, filter_type, category_name, status, product_count, pid)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ''', (full_link, filter_name, filter_type, "Sarees", "pending", product_count, PID))
                        conn.commit()
                        print(f"[{filter_name}] Inserted..")
                    except Exception as insert_err:
                        print(f"[{filter_name}] Insert failed: {insert_err}")
                        continue

                next_pages = selector.xpath(
                    "//span[contains(translate(text(), 'NEXT', 'next'), 'next')]/ancestor::a[contains(@href, 'page=')]")
                if not next_pages:
                    break

        # ✅ Mark as done
        cursor.execute("UPDATE flipkart_filters SET status = 'done' WHERE id = %s", (filter_id,))
        conn.commit()

    except Exception as e:
        print(f"[{filter_name}] Error: {e}")
        cursor.execute("UPDATE flipkart_filters SET status = 'failed' WHERE id = %s", (filter_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def main():
    # Initial connection to fetch pending filters
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Actowiz',
        database='flipkart_saree'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, url, filter_name, filter_type FROM flipkart_filters WHERE status = 'pending' LIMIT 5")

    # cursor.execute("SELECT id, url, filter_name, filter_type FROM flipkart_filters WHERE status = 'pending' AND id=1")
    filters = cursor.fetchall()

    cursor.close()
    conn.close()

    if not filters:
        print("No pending filters found.")
        return

    # Launch threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(process_filter, f) for f in filters]
        for future in as_completed(futures):
            future.result()  # Raises exception if any occurred in threads

    print("✅ All filters processed.")


if __name__ == "__main__":
    main()
