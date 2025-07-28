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
    if response and response.status_code == 200 and 'slAVV4' in response.text:
        return True
    else:
        return False

def save_html(response):

    output_path = r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_computer_response_all.html'
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
    products = selector.xpath('//div[contains(@class,"slAVV4")]')
    print(f"Found {len(products)} products on this page")

    store_data=[]

    for product in products:
        product_name=product.xpath('.//a[@class="wjcEIp"]//text()').getall()  #.//div[@class="store-info-box"]//li[@class="outlet-name"]/div[@class="info-text"]/a/text()
        print(product_name)
        product_detail = product.xpath('.//div[@class="NqpwHC"]//text()').get()
        print(product_detail)
        rating = product.xpath('.//div[@class="XQDdHH"]//text()').get(default='No rating')
        print("rating", rating)
        price = product.xpath('.//div[@class="Nx9bqj"]//text()').get()
        print(price)
        total_reviews = product.xpath('.//span[@class="Wphh3N"]//text()').get(default='No review')
        print("total_reviews", total_reviews)
        img_source = product.xpath('.//div[@class="_4WELSP"]/img[@class="DByuf4"]/@src').get(default='No image to show')
        print(img_source)


        store_dict={

            'product_name':product_name,
             'product_detail':product_detail,
            # 'size':size,
            # 'color':color,
            # 'weight':weight,
            'rating':rating,
            'price':price,
            'total_reviews':total_reviews,
            'img_source':img_source
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
col_names=['product_name','product_detail','rating','price','total_reviews','img_source']
def write_to_csv(all_stored_data_lst,csv_output_path):
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

    for i in range(1, 10):

        url='https://www.flipkart.com/search?q=computer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'+'&page='+str(i)
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


    json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_computer_response_all_for_loop.json'
    write_to_json(all_stored_data_lst, json_output_path)

    csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_computer_csv_using_for_loop.csv'
    write_to_csv(all_stored_data_lst, csv_output_path)

    # dump_csv_to_database(csv_output_path)


