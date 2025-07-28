import requests
import random
import gzip
from parsel import Selector
import json
import time

user_agents_lst = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
]

def create_request(url):
    headers = {
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Request to {url} - Status: {response.status_code}")
        return response
    except Exception as e:
        print(f"Request error: {e}")
        return None

def has_next_page(selector):
    next_button = selector.xpath('//a[contains(text(), "Next") and not(contains(@class, "disabled"))]')
    return bool(next_button)

def parse(raw_html):
    selector = Selector(text=raw_html)
    stores = selector.xpath('//div[@class="store-info-box"]')
    store_data = []

    for store in stores:
        name = store.xpath('.//li[@class="outlet-name"]//text()').getall()
        store_name = next((x.strip() for x in name if x.strip()), None)

        add = store.xpath('.//li[@class="outlet-address"]//text()').getall()
        cleaned_address = [line.strip() for line in add if line.strip()]
        store_address = ', '.join(cleaned_address)

        phone = store.xpath('.//li[@class="outlet-phone"]//text()').getall()
        phone = next((x.strip() for x in phone if x.strip()), None)

        map_link = store.xpath('.//a[@class="btn btn-map"]/@href').get()
        website = store.xpath('.//a[@class="btn btn-website"]/@href').get()

        store_dict = {
            'store_name': store_name,
            'store_address': store_address,
            'phone': phone,
            'map': map_link,
            'website': website
        }

        store_data.append(store_dict)

    return store_data, selector

def write_to_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Saved {len(data)} store records to JSON.")

if __name__ == '__main__':
    all_stores = []
    page = 1

    while True:
        url = f'https://stores.burgerking.in/?page={page}'
        response = create_request(url)
        if response and response.status_code == 200:
            raw_html = response.text
            stores, selector = parse(raw_html)
            all_stores.extend(stores)
            print(f'Parsed {len(stores)} stores from page {page}')

            if has_next_page(selector):
                page += 1
                time.sleep(1)  # Be polite to server
            else:
                print('No more pages. Exiting loop.')
                break
        else:
            print(f"Failed to retrieve page {page}. Exiting.")
            break

    json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_data_by_next.json'
    write_to_json(all_stores, json_output_path)




# import requests
# import random
# import gzip
# from parsel import Selector
# import json
# import os
#
# user_agents_lst = [
#     'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     # Add more if needed
# ]
#
# def create_request(url):
#     headers = {
#         'User-Agent': random.choice(user_agents_lst),
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive',
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         print(f"Request Status ({url}): {response.status_code}")
#         return response
#     except Exception as e:
#         print(f"Error during request: {e}")
#         return None
#
# def check_response(response):
#     return response and response.status_code == 200 and 'store-info-box' in response.text
#
# def parse(raw_html):
#     selector = Selector(text=raw_html)
#     stores = selector.xpath('//div[@class="store-info-box"]')
#
#     store_data = []
#     for store in stores:
#         store_name = store.xpath('.//li[@class="outlet-name"]//text()').get(default='').strip()
#         add = store.xpath('.//li[@class="outlet-address"]//text()').getall()
#         store_address = ', '.join([line.strip() for line in add if line.strip()])
#         phone = store.xpath('.//li[@class="outlet-phone"]//text()').get(default='').strip()
#         map_link = store.xpath('.//a[@class="btn btn-map"]/@href').get(default='')
#         website = store.xpath('.//a[@class="btn btn-website"]/@href').get(default='')
#
#         store_dict = {
#             'store_name': store_name,
#             'store_address': store_address,
#             'phone': phone,
#             'map': map_link,
#             'website': website,
#         }
#         store_data.append(store_dict)
#
#     return store_data, selector
#
# def has_next_page(selector):
#     next_button = selector.xpath('//a[contains(text(), "Next") and not(contains(@class, "disabled"))]')
#     return bool(next_button)
#
#
# # def has_next_page(selector):
# #     # Check if the "Next" button exists and is clickable
# #     next_button = selector.xpath('//a[contains(@class, "next") and not(contains(@class, "disabled"))]')
# #     return bool(next_button)
#
# def write_to_json(data, path):
#     with open(path, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
#     print(f"JSON data written to {path}")
#
# if __name__ == '__main__':
#     all_stored_data_lst = []
#     page = 1
#     base_url = 'https://stores.burgerking.in/?page='
#
#     while True:
#         url = base_url + str(page)
#         response = create_request(url)
#
#         if not check_response(response):
#             print('Response check failed or no more stores. Stopping.')
#             break
#
#         raw_html = response.text
#         page_data, selector = parse(raw_html)
#         all_stored_data_lst.extend(page_data)
#
#         if has_next_page(selector):
#             print(f"Moving to next page: {page + 1}")
#             page += 1
#         else:
#             print("No more pages found. Scraping complete.")
#             break
#
#     json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_data_dynamic.json'
#     write_to_json(all_stored_data_lst, json_output_path)




# import requests
# import random
# import gzip
# from parsel import Selector
# import json
#
#
# user_agents_lst = [
#     'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
# ]
#
#
# def create_request(url):
#
#     # Request headers
#     headers = {
#         'User-Agent': random.choice(user_agents_lst),
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive',
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         print(f"Request Status: {response.status_code}")
#         return response
#     except Exception as e:
#         print(f"Error during request: {e}")
#         return None
#
# def check_response(response):
#     if response and response.status_code == 200 and 'store-info-box' in response.text:
#         return True
#     else:
#         return False
#
# def save_html(response):
#
#     output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_for_loop.html'
#     print(output_path)
#     try:
#         raw_html = response.text
#         print(raw_html)
#         # Write the HTML text as gzip-compressed file
#         with open(output_path, 'w', encoding='utf-8') as file:
#             file.write(raw_html)
#         print("HTML content fetched and written successfully.")
#
#         with open(output_path, 'rb') as file_binary:
#             with gzip.open(output_path + '.gz', 'wb') as file_gzip:
#                 file_gzip.writelines(file_binary)
#         print('file has been saved in compressed zip file.')
#         return raw_html
#
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
#
#
#
# def parse(raw_html):
#     selector = Selector(text=raw_html)
#     stores = selector.xpath('//div[@class="store-info-box"]')
#     print('stores',stores)
#
#
#     store_data=[]
#
#     for store in stores:
#
#         name=store.xpath('.//li[@class="outlet-name"]//text()').getall()
#         store_name = next((x.strip() for x in name if x.strip()), None)
#         # print('Store name:',store_name)
#
#         add=store.xpath('.//li[@class="outlet-address"]//text()').getall()
#         cleaned_address = [line.strip() for line in add if line.strip() != '']
#         store_address=','.join(cleaned_address)
#         # print('store_address',store_address)
#
#         phone=store.xpath('.//li[@class="outlet-phone"]//text()').getall()
#         phone = next((x.strip() for x in phone if x.strip()), None)
#         # print('Contact number:',phone)
#
#         map=store.xpath('.//a[@class="btn btn-map"]/@href').getall()[0]
#         # print('Map link',map)
#
#         website=store.xpath('.//a[@class="btn btn-website"]/@href').getall()[0]
#         # print('website link',website)
#
#         print('//////////////////////////////////////////////')
#
#         store_dict={
#
#             'store_name':store_name,
#             'store_address':store_address,
#             'phone':phone,
#             'map':map,
#             'website':website,
#                   }
#         store_data.append(store_dict)
#     print(store_data)
#     print(len(store_data))
#     return store_data
#
# def write_to_json(all_stored_data_lst,json_output_path):
#     with open(json_output_path, 'w', encoding='utf-8') as json_file:
#         json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
#     print(f"Data saved to {json_output_path}")
#
#
#
# if __name__ == '__main__':
#     all_stored_data_lst=[]
#     # url = "https://stores.burgerking.in/location/gujarat/ahmedabad"
#     # url='https://stores.burgerking.in/'
#     for i in range(1, 86):  # https://stores.burgerking.in/?page=85
#         url = 'https://stores.burgerking.in/'
#         response=create_request(url)
#         if check_response(response):
#             raw_html=save_html(response)
#             if raw_html:
#                 page_data=parse(raw_html)
#                 all_stored_data_lst.extend(page_data)
#
#             else:
#                 print('Failed to save HTML content')
#         else:
#             print('Response check failed. Skipping save and parse steps.')
#
#
#
#     json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_for_loop.json'
#     write_to_json(all_stored_data_lst, json_output_path)
#
#
#
#
#             ############################