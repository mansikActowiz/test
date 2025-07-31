import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine


url='https://locations.starbucks.sa/directory/'



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
col_names=['store_name','store_address','store_link','map_link']
def write_to_csv(all_stored_data_lst,csv_output_path):
    with open(csv_output_path, 'w', encoding='utf-8') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(all_stored_data_lst)
    print(f"Data saved to CSV path:{csv_output_path}")


output_path = r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_html.html'
print(output_path)

raw_html=response.text


with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

selector = Selector(text=raw_html)

state_name=selector.xpath('//section[@class="Directory Directory--ace CityList"]//li[@class="Directory-listItem"]//span[@class="Directory-listLinkText"]/text()').getall()
state_name= [item.lower() for item in state_name]
print(state_name)

all_store_lst=[]
for state in state_name:
    state_url=url+state
    print("state_url",state_url)#https://locations.starbucks.sa/directory/abha
    state_response = requests.get(state_url, headers=headers)
    print(f"Request Status: {response.status_code}")
    state_raw_html=state_response.text
    selector1 = Selector(text=state_raw_html)
    stores = selector1.xpath('//div[@class="Teaser--nearby"]')
    print(f"Found {len(stores)} stores on this page")


    for j in stores:
        store_name = j.xpath('.//h2[@class="Teaser-title"]/text()').get()
        print('store_name', store_name)
        store_address=j.xpath('.//div[@class="Teaser-address"]/address[@class="c-address"]//text()').get()
        print('store_add', store_address)
        store_link=j.xpath('.//a/@href').get()
        store_link='https://locations.starbucks.sa'+store_link[2:]
        print('store_link', store_link)
        map_link=j.xpath('.//div[@class="c-get-directions"]//a/@href').get()
        print('map_link', map_link)
        store_dict = {

        'store_name': store_name,
        'store_address': store_address,
        'store_link': store_link,
        'map_link': map_link

             }
        all_store_lst.append(store_dict)


json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_all_stores.json'
write_to_json(all_store_lst,json_output_path)

csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_all_stores.csv'
write_to_csv(all_store_lst,csv_output_path)

exit(0)





# state_url_lst.append(state_url)
# print(len(state_url_lst))
# exit(0)
# state_names=selector.xpath('//div[@class="Directory-content"]/text()').getall()
# print(state_names)
# exit(0)
#
# '''remove empty element in list'''
# cleaned_states = [state for state in state_names if state]
# print(cleaned_states)
#
#
# all_stored_data_lst = []
#
# for state in cleaned_states:
#     state_url=f'https://store.croma.com/getCitiesByMasterOutletIdAndStateName.php?master_outlet_id=247436&state_name={state}'
#     print(state_url)
#     state_response = requests.get(state_url, headers=headers)
#     print(f"states Request Status: {state_response.status_code}")
#     state_txt=state_response.text
#     print('cities of states',state_txt)
#     print('cities of states',type(state_txt))
#     cities_of_states = json.loads(state_txt)
#     print(cities_of_states)
#
#     for key, value in cities_of_states.items():
#         print(f"Key: {key} ➤ Value: {value}")
#         exit(0)
#         city_url=f'https://store.croma.com/getLocalitiesByMasterOutletIdAndCityName.php?master_outlet_id=247436&city_name={key}'
#         city_response = requests.get(city_url, headers=headers)
#         print(f"Request Status of city: {city_response.status_code}")
#         city_txt=city_response.text
#         print(city_txt)
#         print('localities of city',type(city_txt))
#
#
#
#         localities_of_cities = json.loads(city_txt)
#         print(localities_of_cities)
#         for key1, value1 in localities_of_cities.items():
#             print(f"Key: {key1} ➤ Value: {value1}")
#
#
#
#             final_path=f'https://store.croma.com/location/{state}/{key}/{key1}'
#             print(final_path)
#
#             final_response=requests.get(final_path, headers=headers)
#             # final_response = requests.get(final_response, headers=headers)
#             print(f"Request Status of final_path: {final_response.status_code}")
#
#             final_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\final_croma_response_html.html'
#             print(final_output_path)
#
#             my_raw_html = final_response.text
#             # print(raw_html)
#
#             with open(final_output_path, 'w', encoding='utf-8') as file:
#                 file.write(my_raw_html)
#             print("final HTML content fetched and written successfully.")
#
#             with open(final_output_path, 'rb') as file_binary:
#                 with gzip.open(final_output_path + '.gz', 'wb') as file_gzip:
#                     file_gzip.writelines(file_binary)
#             print('final file has been saved in compressed zip file.')
#
#             selector = Selector(text=my_raw_html)
#             products = selector.xpath('//div[@class="store-info-box"]')
#             print(f"Found {len(products)} products on this page")
#
#             home_page = selector.xpath('//div[@class="store-info-box"]')
#             store_data = []
#             for i in home_page:
#
#                 name = i.xpath('.//div[@class="info-text"]/a[@href]/text()').getall()
#                 cleaned_name = [line.strip() for line in name if line.strip() != '']
#                 store_name = ','.join(cleaned_name)
#                 print(store_name)
#                 add = i.xpath('.//li[@class="outlet-address"]/div[@class="info-text"]//text()').getall()
#                 print('add', add)
#                 cleaned_address = [line.strip() for line in add if line.strip() != '']
#                 store_address = ','.join(cleaned_address)
#                 print('store_address:', store_address)
#                 phone = i.xpath('.//li[@class="outlet-phone"]//text()').getall()
#                 store_phone = [p.strip() for p in phone if p.strip()][0]
#                 print('phone', store_phone)
#                 timing = i.xpath('.//li[@class="outlet-timings"]//text()').getall()
#                 store_timing = [t.strip() for t in timing if t.strip()][0]
#                 print('timing',store_timing)
#                 store_dict = {
#
#                     'store_name': store_name,
#                     'store_address': store_address,
#                     'store_phone': store_phone,
#                     'store_timing': store_timing,
#
#                 }
#                 store_data.append(store_dict)
#             all_stored_data_lst.extend(store_data)
#             print(store_data)
#             print(len(store_data))
#
# with open(r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\final_croma_response_json_new.json', 'w', encoding='utf-8') as json_file:
#     json.dump(all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
# print(f"Data saved to JSON path: {r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\final_croma_response_json_new.json'}")
#
