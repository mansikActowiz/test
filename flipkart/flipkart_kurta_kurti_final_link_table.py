import mysql.connector
import time
import random
from curl_cffi import requests
from parsel import Selector
import os
import gzip

cookies = {
    'T': 'TI175463037559600185559379502332393567354467573374801932499086629278',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20309%7CMCMID%7C69546711188423189499195618647822413963%7CMCAAMLH-1755235148%7C12%7CMCAAMB-1755235148%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754637548s%7CNONE%7CMCAID%7CNONE',
    'vw': '1366',
    'dpr': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwODExNDIwMTQ3ODhQM0xLSEsiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDQxMzUyMSwiaWF0IjoxNzU0NjMzNTIxLCJqdGkiOiIxMjFlZTg1OS1jZjdmLTRjM2QtODk4OC0yMzUyZmYwYzEzNjUifQ.cE4WOweV-FpAHgC-MkfN2E_AsT6MDJuNEVmaOPx7Ybk',
    'ud': '7._EA8MPay8RgQCnXpsBXZHK5sc7gILo9FHj0aYgGHR1Oumr39zAo6t-7vuMSHXlmkUuxx5a6dthHiykOKVmj8-6JYMhAE-R64QEhI0aPsJh1tmTBdRrKHxyGGBvwc8qOhoUS2I2Momh6PF2Sb1hlfFy4n2wuS5aUifxkiWIztG_FDaKHAfmpyhrEN0l4YXrd1',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NTQ2NDY0MDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNDRjYTdhOTItZWExMC00NzA5LTg1MWYtMGRjMDYxYzhhN2IxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IjZKei0tRjl5ZHNzcl82bU5xc0JRa0x3VlNUUXktbkpaazlzandzdURVRzBXRVJVa2NGQ285QT09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YsA4hIT78xjyfM76wBtuVqaF248o9vjKmKY4EKC1_Pc',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzA1NDIyMDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNWI3ODIyZGItOGMzZi00NTFhLTkzN2EtYmFmNjlmNzQ4MWMxIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiS1hQRk1ZIn0.jQbJsjVpfS-Uq5psFGV7IN-qomGHeU3Cy8dEcxYEpXs',
    'K-ACTION': 'null',
    'vh': '607',
    'qH': '5985e3313e9e348f',
    'Network-Type': '3g',
    'vd': 'VI3B15274DB9524B47B106991AAB1770AC-1754630379676-4.1754646255.1754644605.151586550',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'S': 'd1t17Pz9VLT82fTF0URASP0QMaqC4cY3y61lcFfIXUG1iExF6OZtX06RaFs3wUQSztb/D93DQoDdAsRyXWVuVJ01hVg==',
    'SN': 'VI3B15274DB9524B47B106991AAB1770AC.TOK67B1C0DAE9A44B1CBA5210AF3BAAED43.1754646303581.LI',
}


user_agents_lst = [
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]

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
    # 'Cookie': 'T=TI175463037559600185559379502332393567354467573374801932499086629278; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20309%7CMCMID%7C69546711188423189499195618647822413963%7CMCAAMLH-1755235148%7C12%7CMCAAMB-1755235148%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754637548s%7CNONE%7CMCAID%7CNONE; vw=1366; dpr=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwODExNDIwMTQ3ODhQM0xLSEsiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDQxMzUyMSwiaWF0IjoxNzU0NjMzNTIxLCJqdGkiOiIxMjFlZTg1OS1jZjdmLTRjM2QtODk4OC0yMzUyZmYwYzEzNjUifQ.cE4WOweV-FpAHgC-MkfN2E_AsT6MDJuNEVmaOPx7Ybk; ud=7._EA8MPay8RgQCnXpsBXZHK5sc7gILo9FHj0aYgGHR1Oumr39zAo6t-7vuMSHXlmkUuxx5a6dthHiykOKVmj8-6JYMhAE-R64QEhI0aPsJh1tmTBdRrKHxyGGBvwc8qOhoUS2I2Momh6PF2Sb1hlfFy4n2wuS5aUifxkiWIztG_FDaKHAfmpyhrEN0l4YXrd1; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NTQ2NDY0MDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNDRjYTdhOTItZWExMC00NzA5LTg1MWYtMGRjMDYxYzhhN2IxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IjZKei0tRjl5ZHNzcl82bU5xc0JRa0x3VlNUUXktbkpaazlzandzdURVRzBXRVJVa2NGQ285QT09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YsA4hIT78xjyfM76wBtuVqaF248o9vjKmKY4EKC1_Pc; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzA1NDIyMDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNWI3ODIyZGItOGMzZi00NTFhLTkzN2EtYmFmNjlmNzQ4MWMxIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiS1hQRk1ZIn0.jQbJsjVpfS-Uq5psFGV7IN-qomGHeU3Cy8dEcxYEpXs; K-ACTION=null; vh=607; qH=5985e3313e9e348f; Network-Type=3g; vd=VI3B15274DB9524B47B106991AAB1770AC-1754630379676-4.1754646255.1754644605.151586550; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; S=d1t17Pz9VLT82fTF0URASP0QMaqC4cY3y61lcFfIXUG1iExF6OZtX06RaFs3wUQSztb/D93DQoDdAsRyXWVuVJ01hVg==; SN=VI3B15274DB9524B47B106991AAB1770AC.TOK67B1C0DAE9A44B1CBA5210AF3BAAED43.1754646303581.LI',
}

params = {
    'sid': 'clo,cfv,cib,rkt',
    'q': 'kurtas kurtis',
    'otracker': [
        'categorytree',
        'nmenu_sub_Women_0_Kurtas & Kurtis',
    ],
}



base_url='https://www.flipkart.com/clothing-and-accessories/ethnic-wear/kurtas/women-kurtas-and-kurtis/pr?sid=clo,cfv,cib,rkt&q=kurtas+kurtis&otracker=categorytree&otracker=nmenu_sub_Women_0_Kurtas%20%26%20Kurtis'



response = requests.get(base_url,
    params=params,
    cookies=cookies,
    impersonate="chrome110",
    headers=headers,
)
print(response.status_code)


time.sleep(random.uniform(1, 5))

sort_by_list = ['relevance','popularity','price_asc', 'price_desc', 'recency_desc']


# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Actowiz',
    database='flipkart_kurta_kurti'
)
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT id, url, filter_name, filter_type FROM flipkart_kurta_kurti_filters  WHERE status = 'pending' AND id=7 ")
# cursor.execute("SELECT id, url, filter_name, filter_type FROM flipkart_filters WHERE status = 'pending' limit 1")
filters = cursor.fetchall()
print(filters)

for filter_row in filters:
    print(filter_row)
    # exit(0)
    filter_id = filter_row['id']
    url = filter_row['url']
    print(url)
    filter_name = filter_row['filter_name']
    filter_type = filter_row['filter_type']

    try:
        response = requests.get(url, cookies=cookies, headers=headers, impersonate="chrome110")
        print(f"[{filter_name}] Status: {response.status_code}")

        if response.status_code != 200:
            raise Exception("Failed to fetch initial page")

        selector = Selector(text=response.text)
        visible_site_count = selector.xpath('.//span[@class="BUOuZu"]//text()').get()
        print('visible_site_count',visible_site_count)
        product_count= visible_site_count.split(' ')[-4] if visible_site_count else "0"
        product_count = int(product_count.replace(',', ''))
        print(product_count)



        if int(product_count) > 1000:
            page_urls = [(f"{url}&sort={sort}&page=0",sort) for sort in sort_by_list]
        else:
            page_urls = [(f"{url}&page=0",None)]
        for page_url,sort in page_urls:
            for page_num in range(1,26):
                page_url = f"{page_url.split("&page=")[0]}&page={page_num}"
                # print(f"Request on: {page_url} on Page: {page_num}")
                res = requests.get(page_url, cookies=cookies, headers=headers)
                if res.status_code != 200:
                    # print("Failed to fetch page, skipping.")
                    continue
                raw_html = res.text

                html_dir = rf'D:\flipkart\flipkart_kurta_kurti_html'
                os.makedirs(html_dir, exist_ok=True)

                sort_suffix = f"_{sort}" if sort else ""
                safe_filter_name = filter_name.replace(" ", "_")
                filename = f"kurta_kurti_{safe_filter_name}{sort_suffix}_page{page_num}.html"
                html_path = os.path.join(html_dir, filename)

                # Save HTML and GZ
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(raw_html)

                with open(html_path, 'rb') as fb:
                    with gzip.open(html_path + '.gz', 'wb') as fg:
                        fg.writelines(fb)


                selector = Selector(text=raw_html)
                products = selector.xpath('//div[@class="_1sdMkc LFEi7Z"]')
                for item in products:
                    relative_link = item.xpath('.//a/@href').get()
                    if not relative_link:
                        continue
                    full_link = 'https://www.flipkart.com' + relative_link
                    # print('full_link.....',full_link)

                    PID = relative_link.split("?pid=")[-1].split("&")[0].strip()
                    # Insert one product link at a time
                    try:
                        cursor.execute('''
                            INSERT INTO kurta_kurti_product_links 
                            (product_link, filter_name, filter_type, category_name, status,product_count, pid)
                            VALUES (%s, %s, %s, %s, %s,%s, %s)
                        ''', (full_link, filter_name, filter_type, "Kurta & Kurti", "pending",product_count, PID))
                        conn.commit()
                        print(f"Inserted", )
                    except Exception as insert_err:
                        print(f"Failed to insert product link: {insert_err}")
                        continue  # skip to next product
                next_pages = selector.xpath(
                    "//span[contains(translate(text(), 'NEXT', 'next'), 'next')]/ancestor::a[contains(@href, 'page=')]")
                if not next_pages:
                    break
        # ✅ If everything went well, mark filter as done
        cursor.execute("UPDATE flipkart_kurta_kurti_filters SET status = 'done' WHERE id = %s", (filter_id,))
        conn.commit()

    except Exception as e:
        print(f"Error processing filter [{filter_name}]: {e}")
        # ❌ Update status to failed
        cursor.execute("UPDATE flipkart_kurta_kurti_filters SET status = 'failed' WHERE id = %s", (filter_id,))
        conn.commit()

# Close connection
cursor.close()
conn.close()
print("Finished processing filters.")
