import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine





# url="https://store.croma.com/"
url='https://store.croma.com/location/gujarat/ahmedabad/shyamal-cross-road'
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
    'User-Agent': random.choice(user_agents_lst),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}
try:
    response = requests.get(url, headers=headers)
    print(f"Request Status: {response.status_code}")
except Exception as e:
    print("no response found")

output_path = path=r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\croma_store_locator_html.html'
print(output_path)

raw_html=response.text
# print(raw_html)
# exit(0)
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

selector = Selector(text=raw_html)
# print(selector)
products = selector.xpath('//div[@class="store-info-box"]')
print(f"Found {len(products)} products on this page")

home_page = selector.xpath('//div[@class="store-info-box"]')
for i in home_page:
 # name=i.xpath('.//div[@class="slAVV4"]/a[@class="wjcEIp"]/@title').getall()
 name = i.xpath('.//div[@class="info-text"]/a[@href]/text()').getall()
 print('//////////////')
 print('name',name)
 cleaned_name = [line.strip() for line in name if line.strip() != '']
 store_name = ','.join(cleaned_name)
 print(store_name)


 add=i.xpath('.//li[@class="outlet-address"]/div[@class="info-text"]//text()').getall()
 print('add',add)
 cleaned_address = [line.strip() for line in add if line.strip() != '']
 store_address = ','.join(cleaned_address)
 print('store_address:',store_address)
 phone=i.xpath('.//li[@class="outlet-phone"]//text()').getall()
 phone=[p.strip() for p in phone if p.strip() ][0]
 print('phone',phone)
 timing=i.xpath('.//li[@class="outlet-timings"]//text()').getall()
 timing=[t.strip() for t in timing if t.strip()][0]
 print('timing',timing)
 # direction=i.xpath('.//li[@class="outlet-actions"]/a[@class="btn btn-call"]//text()').getall()
 # print('direction',direction)


