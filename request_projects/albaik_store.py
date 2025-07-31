import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine
import csv


url='https://www.al-baik.com/restaurants'
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

# output_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\croma_response_html.html'
output_path=r'C:\Users\Madri.Gadani\Desktop\madri\albaik_store\albaik_store_all_html.html'
print(output_path)

raw_html=response.text
# print(raw_html)

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

selector = Selector(text=raw_html)
state_name=selector.xpath('//div[@class="col-md-3 d-md-block d-none"]/div[@class="list-group list-group-flush mb-md-4 mb-3"]/a/text()').getall()
print(state_name)

for state in state_name:
    print(state)

    state_url = url+f'/{state}'
    print(state_url)

    state_response = requests.get(state_url, headers=headers)
    print(f"states Request Status: {state_response.status_code}")
    state_html = state_response.text

    with open(r'C:\Users\Madri.Gadani\Desktop\madri\albaik_store\albaik_store_all_html1.html', 'w', encoding='utf-8') as file:
        file.write(state_html)
    print("HTML content fetched and written successfully.")

    selector = Selector(text=state_html)
    # city = selector.xpath('.//a[@class="list-group-item border-0 shadow-sm "]/text()').getall()
    city=selector.xpath('//div[@class="col-md-3 d-md-block d-none"]//div[@class="list-group list-group-flush mb-md-4 mb-3"]/a/following-sibling::div//a/text()').getall()
    print(city)
    exit(0)
    # print(f"Found {len(products)} products on this page")

    exit()
    # // a[ @
    #
    #
    # class ="list-group-item border-0 shadow-sm "]
    # exit(0)
    # print('cities of states', type(state_txt))
    # cities_of_states = json.loads(state_txt)
    # # print(cities_of_states)
    #
    # for key, value in cities_of_states.items():
    #     print(f"Key: {key} ➤ Value: {value}")
    #     exit()
    #     city_url=url+f'{state}/{key}'
    #     print(city_url)
    #     exit(0)
    #     city_response = requests.get(city_url, headers=headers)
    #     print(f"Request Status of city: {city_response.status_code}")
    #     city_txt=city_response.text
    #     localities_of_cities = json.loads(city_txt)
    # exit()
    #


# stores = selector.xpath('//div[@class="Teaser--nearby"]')
# print(f"Found {len(stores)} stores on this page")
# exit(0)
#
# home_page = selector.xpath('//div[@class="Teaser--nearby"]')
# for i in home_page:
#     name =selector.xpath('.//h2[@class="Teaser-title"]/text()').get()
#     print('name', name)
#     time=selector.xpath('.//span[@class="Hours-statusText"]//text()').getall()
#     print('time', time)
#     add=selector.xpath('.//div[@class="Teaser-address"]/text()').getall()
#     print('add', add)
#     direction=selector.xpath('.//div[@class="c-get-directions-button-wrapper"]/a/@href').getall()
#     print('direction', direction)
# exit(0)
