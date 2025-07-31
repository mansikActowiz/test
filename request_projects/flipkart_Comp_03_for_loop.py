import json
import csv
from curl_cffi import requests
import random
import gzip
from parsel import Selector
import os
# from fake_useragent import UserAgent

# ua=UserAgent()

# url='https://www.flipkart.com/search?q=computer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'



def write_to_json(all_stored_data_lst,json_output_path):
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to JSON path: {json_output_path}")


col_names=['product_name', 'product_url', 'product_original_price', 'product_discount', 'product_price', 'delivery_date', 'star', 'rating', 'review', 'highlights', 'description', 'img_source', 'specification','bank_offers']
def write_to_csv(all_stored_data_lst,csv_output_path):
    with open(csv_output_path, 'w', encoding='utf-8') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(all_stored_data_lst)
    print(f"Data saved to CSV path:{csv_output_path}")


output_path = r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_new_10_pages'


for i in range(1,11):
 url = 'https://www.flipkart.com/search?q=computer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'+'&page='+str(i)
 print(url)
 user_agents_lst = [
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # Add more user agents if needed
        ]
 headers = {
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
     'User-Agent': random.choice(user_agents_lst),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive'}
 try:
    response = requests.get(url, headers=headers,impersonate="chrome120",timeout=15,)
    print(f"Request Status: {response.status_code} for page {i}")

    if response.status_code == 200:
        html_path=os.path.join(output_path,f'page_no_{i}_html.html')
        raw_html = response.text

        # Save HTML file
        with open(html_path, 'w', encoding='utf-8' ) as file:
            file.write(raw_html)
        print(f"HTML content fetched and written successfully for page {html_path}.")

        # Save as gzip
        gz_html_path = os.path.join(output_path,f'page_no_{i}_gz.gz')
        with open(html_path, 'rb') as file_binary:
            with gzip.open(gz_html_path, 'wb') as file_gzip:
                file_gzip.writelines(file_binary)
        print(f'File has been saved in compressed zip file for page {gz_html_path}.')

        selector = Selector(text=raw_html)


        product = selector.xpath('//div[contains(@class,"slAVV4")]').getall()
        print(f"Found {len(product)} products on this page {i}")






    else:
        print(f'failed to fetch data for page {i}')


 except Exception as e:(
    print(f"Error while making request for page {i}:,{e}" ))
exit(0)
