import requests
import random
import gzip
from parsel import Selector
import json
import csv
import re
import pandas as pd
from sqlalchemy import create_engine


url='https://sankalprestaurants.com/south-indian-restaurant-near-me/'



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}



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


def write_to_json(all_stored_data_lst,json_output_path):
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to JSON path: {json_output_path}")



'''function to write list of  dictionary into csv'''

col_names=['store_name','store_address','store_link','map_link','phone_number_site','phone']
def write_to_csv(all_stored_data_lst,csv_output_path):
    with open(csv_output_path, 'w', encoding='utf-8') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(all_stored_data_lst)
    print(f"Data saved to CSV path:{csv_output_path}")


output_path = r'C:\Users\Madri.Gadani\Desktop\madri\sankalp\sankalp_html.html'
print(output_path)

raw_html=response.text

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

print(url)

selector = Selector(text=raw_html)
country=selector.xpath('//div[@class="jet-smart-filters-hierarchy jet-filter "]//select[@class="jet-select__control depth-0"]/option/text()').getall()
country_name=country[1:]
print(country_name)


for i in country_name:


    state=selector.xpath('//div[@class="jet-smart-filters-hierarchy jet-filter "]//select[@class="jet-select__control depth-1"]/option/text()').getall()

    # state_name=state[1:]
    print(state)
    exit()




#
#
#
#
# all_cities_link=selector.xpath('//div[@class="padding-0-mob col-sm-3 col-md-2 col-lg-2 hidden-xs"]//a/@href').getall()
#
#
# all_store_lst = []
#
# for city in all_cities_link:
#     print(city)                                 #/store-location/new-delhi
#
#     city_name = city.split('/')[-1]
#     print(city_name)
#
#     new_url='https://www.dominos.co.in'+city
#     response_city=requests.get(new_url)
#     city_html=response_city.text
#     city_selector=Selector(text=city_html)
#
#     all_store=city_selector.xpath('//div[@class="panel panel-default custom-panel"]')
#     print(f"Total Domino's outlet: {len(all_store)} in {city_name}  city")  #it will count no of outlets in particular city
#
#     for j in all_store:
#         store_area=j.xpath('.//div[@class="media-body"]//p/text()').get()
#         print(f"Location:{city_name}-",store_area)
#         store_name=j.xpath('.//a[@href]/h2/text()').get()
#         print("Store Name:",store_name)
#         store_address=j.xpath('.//div[@class="media-body"]/p[@class="grey-text mb-0"]/text()').get()
#         print("Store Address:",store_address)
#         store_link = j.xpath('.//div[@class="media-body"]/a/@href').get()
#         store_link='https://www.dominos.co.in'+store_link
#         print("Store_link:", store_link)
#
#         store_response=requests.get(store_link)
#         # print(store_response.status_code)
#
#         store_html=store_response.text
#         store_selector=Selector(text=store_html)
#
#         store_phone=store_selector.xpath('//div[@class="tab-content cus-tab-content"]//div[@class="phone mb-20"]/a/p/text()').get()
#         print("Store_phone",store_phone)
#         store_map_link=store_selector.xpath('//div[@class="get-map-box padding-0"]/a/@href').get()
#         print("Store_map_link",store_map_link)
#         store_time=store_selector.xpath('//div[@class="col-xs-6 col-sm-4 col-md-4 col-lg-4 padding-0"]//div[@class="phone mb-20"]/p/text()').get()
#         print("Store_time",store_time)
#         print(f'//////////////////////////////Next Location of  {city_name}////////////////////////////////////////////////////')
#
#
#
#         store_dict = {
#         'city':city_name,
#         'store_area':store_area,
#         'store_name': store_name,
#         'store_address': store_address,
#         'store_phone':store_phone,
#         'store_link': store_link,
#         'store_map_link': store_map_link,
#         'store_time': store_time,
#
#              }
#         all_store_lst.append(store_dict)
# exit(0)
#
# json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\dominos\dominos_json.json'
# write_to_json(all_store_lst,json_output_path)
#
# csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\dominos\dominos_csv.csv'
# df=pd.read_json(csv_output_path)
# df.to_csv(csv_output_path,index=false)
