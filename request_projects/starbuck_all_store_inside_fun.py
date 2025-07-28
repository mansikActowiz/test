import requests
import random
import gzip

from bs4 import BeautifulSoup
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
def create_reuest(url):
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


def check_response(response):
    if response and response.status_code == 200 :
        return response.text
        return True
    else:
        return False



def save_html(response):
    output_path = r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_html.html'
    try:
        raw_html = response.text
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(raw_html)
    print("HTML content fetched and written successfully.")

    with open(output_path, 'rb') as file_binary:
        with gzip.open(output_path + '.gz', 'wb') as file_gzip:
            file_gzip.writelines(file_binary)
    print('file has been saved in compressed zip file.')




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


# output_path = r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_html.html'
# print(output_path)

# raw_html=response.text

def main(raw_html):
    url = 'https://locations.starbucks.sa/directory/'
    response=create_reuest
    check_response(response)
    save_html(response)




# def parse(raw_html):
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

            store_url=store_link
            print('store_url', store_url)
            store_response=requests.get(store_url, headers=headers)
            print(f"Request Status: {response.status_code}")
            store_raw_html=store_response.text
            selector2 = Selector(text=store_raw_html)
            phone=selector2.xpath('//div[@class="HeroCore-ctaContainer"]//div[@class="Phone Phone--main"]//a/@href').get()
            print('phone', phone)
            phone_number_site=selector2.xpath('//div[@class="HeroCore-ctaContainer"]//div[@class="Phone Phone--main"]//text()').get()
            print('phone_number_site', phone_number_site)


            store_dict = {

            'store_name': store_name,
            'store_address': store_address,
            'store_link': store_link,
            'map_link': map_link,
            'phone_number_site': phone_number_site,
            'phone': phone,

                 }

            all_store_lst.append(store_dict)


json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_all_stores1.json'
write_to_json(all_store_lst,json_output_path)

csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_all_stores1.csv'
write_to_csv(all_store_lst,csv_output_path)

exit(0)



