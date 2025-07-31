import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine

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


def create_request(url):

    headers = {
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Request Status: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error during request: {e}")
        return None

def check_response(response):
    if response and response.status_code == 200 and 'store-info-box' in response.text:
        return True
    else:
        return False

def save_html(response):

    output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_response_using_for_loop.html'
    print(output_path)
    try:
        raw_html = response.text

        '''Write  HTML text as gzip-compressed file'''
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(raw_html)
        print("HTML content fetched and written successfully.")

        with open(output_path, 'rb') as file_binary:
            with gzip.open(output_path + '.gz', 'wb') as file_gzip:
                file_gzip.writelines(file_binary)
        print('file has been saved in compressed zip file.')
        return raw_html


    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse(raw_html):
    selector = Selector(text=raw_html)
    stores = selector.xpath('//div[@class="store-info-box"]')
    print('stores',stores)

    store_data=[]

    for store in stores:
        name=store.xpath('.//li[@class="outlet-name"]//text()').getall()  #.//div[@class="store-info-box"]//li[@class="outlet-name"]/div[@class="info-text"]/a/text()
        store_name = next((x.strip() for x in name if x.strip()), None)
        # print('Store name:',store_name)

        add=store.xpath('.//li[@class="outlet-address"]//text()').getall()
        cleaned_address = [line.strip() for line in add if line.strip() != '']
        store_address=','.join(cleaned_address)
        # print('store_address',store_address)

        phone=store.xpath('.//li[@class="outlet-phone"]//text()').getall()
        phone = next((x.strip() for x in phone if x.strip()), None)
        # print('Contact number:',phone)

        map=store.xpath('.//a[@class="btn btn-map"]/@href').getall()[0]
        # print('Map link',map)

        website=store.xpath('.//a[@class="btn btn-website"]/@href').getall()[0]
        # print('website link',website)

        store_dict={

            'store_name':store_name,
            'store_address':store_address,
            'phone':phone,
            'map':map,
            'website':website,
                  }
        store_data.append(store_dict)
    print(store_data)
    print(len(store_data))
    return store_data

'''function to write list of dictionary into json'''
def write_to_json(all_stored_data_lst,json_output_path):
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to JSON path: {json_output_path}")

'''function to write list of  dictionary into csv'''
col_names=['store_name','store_address','phone','map','website']
def write_to_csv(all_stored_data_lst,csv_output_path):
    for store in all_stored_data_lst:
        phone = store.get('phone', '').strip()
        if phone.startswith('+'):
            # Add a single quote to make Excel treat it as text
            store['phone'] = "'" + phone

    with open(csv_output_path, 'w', encoding='utf-8') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(all_stored_data_lst)
    print(f"Data saved to CSV path:{csv_output_path}")



def dump_csv_to_database(csv_output_path):
    database_table_name='burger_king_all_store_table'

    df=pd.read_csv(csv_output_path)

    user="root"
    password="Actowiz"
    host="localhost"
    database="burger_king_all_store_locator_db"

    engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    connection = engine.connect()
    print("Connection successful")
    df.to_sql(database_table_name, con=engine, if_exists='replace', index=False)
    print(f"Data inserted successfully into '{database_table_name}' table in '{database}' database.")

if __name__ == '__main__':
    all_stored_data_lst=[]

    # url='https://stores.burgerking.in/'
    for i in range(1, 86):  # https://stores.burgerking.in/?page=85 for reference
        url = 'https://stores.burgerking.in/?page=' + str(i)
        response=create_request(url)
        if check_response(response):
            raw_html=save_html(response)
            if raw_html:
                page_data=parse(raw_html)
                all_stored_data_lst.extend(page_data)
            else:
                print('Failed to save HTML content')
        else:
            print('Response check failed. Skipping save and parse steps.')


    json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_data_using_for_loop.json'
    write_to_json(all_stored_data_lst, json_output_path)

    csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_csv_using_for_loop.csv'
    write_to_csv(all_stored_data_lst, csv_output_path)

    dump_csv_to_database(csv_output_path)


