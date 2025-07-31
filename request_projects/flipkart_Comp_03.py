import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd


import requests
import random
import gzip
from parsel import Selector
import os

url='https://www.flipkart.com/search?q=computer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'



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


output_path = r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_new\flipkart_computer_response_all.html'
gz_output_path = output_path + '.gz'

# Check if HTML file already exists
if os.path.exists(output_path):
    print("HTML file already exists. Reading from the file.")
    with open(output_path, 'r', encoding='utf-8') as file:
        raw_html = file.read()
else:
    print("HTML file not found. Making request to fetch data...")

    url = 'https://www.flipkart.com/search?q=computer&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'
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
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Request Status: {response.status_code}")
        raw_html = response.text

        # Save HTML file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(raw_html)
        print("HTML content fetched and written successfully.")

        # Save as gzip
        with open(output_path, 'rb') as file_binary:
            with gzip.open(gz_output_path, 'wb') as file_gzip:
                file_gzip.writelines(file_binary)
        print('File has been saved in compressed zip file.')

    except Exception as e:
        print("Error while making request:", e)
        raw_html = ""

# Continue parsing
if raw_html:
    selector = Selector(text=raw_html)


    product = selector.xpath('//div[contains(@class,"slAVV4")]')
    print(f"Found {len(product)} products on this page")

    product_name1 = selector.xpath('.//a[@class="wjcEIp"]//text()').getall()  # .//div[@class="store-info-box"]//li[@class="outlet-name"]/div[@class="info-text"]/a/text()
    print('product_name',product_name1)

    product_url = selector.xpath('.//a[@class="wjcEIp"]/@href').getall()
    print('product_url',product_url)

    all_product_lst=[]
    for i in product_url:
        new_url='https://www.flipkart.com'+i
        print(new_url)
        product_response = requests.get(new_url)
        print(product_response.status_code)
        if product_response.status_code == 200:
            raw_html_product = product_response.text
            product_selector = Selector(text=raw_html_product)

            product_name=product_selector.xpath('.//span[@class="VU-ZEz"]/text()').get()
            final_product = product_name.strip() if product_name else ''

            print('product_name',product_name)

            product_price=product_selector.xpath('.//div[@class="Nx9bqj CxhGGd"]/text()').get()
            print('product_price',product_price)

            product_original_price_list = product_selector.xpath('.//div[@class="yRaY8j A6+E6v"]/text()').getall()

            if len(product_original_price_list) >= 2:
                product_original_price = product_original_price_list[0] + product_original_price_list[1]
                print('product_original_price', product_original_price)
            elif len(product_original_price_list) == 1:
                product_original_price = product_original_price_list[0]
                print('product_original_price', product_original_price)
            else:
                product_original_price = None  # or "N/A"
                print('product_original_price', product_original_price)

            product_discount=product_selector.xpath('.//div[@class="UkUFwK WW8yVX"]//text()').get()
            print('product_discount',product_discount)
            if not product_discount:
                product_discount = None  # or "N/A"
                print('product_discount', product_discount)

            delivery_date=product_selector.xpath('//span[@class="Y8v7Fl"]//text()').get()
            print('delivery_date',delivery_date)

            star=product_selector.xpath('.//div[@class="XQDdHH"]/text()').get()
            print('star',star)


            model_number=product_selector.xpath('//table//tr[td[1][contains(text(), "Model Number")]]//li[@class="HPETK2"]').get()
            print('model_number',model_number)

            rr=product_selector.xpath('//div[@class="_5OesEi HDvrBb"]/span[@class="Wphh3N"]//text()').getall()
            print(rr)

            if rr:
                rating=rr[0]
                print('rating',rating)
                review=rr[-1]
                print('review',review)
            else:
                rating = None
                review = None

            highlights=product_selector.xpath('//div[@class="U+9u4y"]//text()').getall()
            highlights=highlights[1:]
            print('highlights',highlights)

            description=product_selector.xpath('//div[@class="cPHDOP col-12-12"]/div[@class="Xbd0Sd"]//p/text()').get()
            print('description',description)

            rows = product_selector.xpath('//table[@class="_0ZhAN9"]/tbody/tr')

            specifications = {}
            for row in rows:
                key = row.xpath('./td[1]//text()').get()
                value = row.xpath('./td[2]//text()').getall()
                key = key.strip() if key else None
                value = ' '.join([v.strip() for v in value if v.strip()])
                if key and value:
                    specifications[key] = value

            bank_offers = product_selector.xpath('//div[@class="NYb6Oz"]//li//text()').getall()
            cleaned_offers = [offer.strip() for offer in bank_offers if offer.strip()]
            print('cleaned_offers',cleaned_offers)

            img_source = product_selector.xpath('.//div[@class="_4WELSP"]/img[@class="DByuf4"]/@src').getall()
            print(img_source)


            store_dict = {

                'product_name':product_name,
                 'product_url':new_url,
                'product_original_price':product_original_price,
                'product_discount':product_discount,
                'product_price':product_price,
                'delivery_date':delivery_date,
                'star':star,
                'rating':rating,
                'review':review,
                'highlights':highlights,
                'description':description,
                'img_source':img_source,
                'specification':specifications,
                'bank_offers':cleaned_offers



                      }
            print(store_dict.keys())

            all_product_lst.append(store_dict)

    print(all_product_lst)



json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_new\flipkart_json1.json'
write_to_json(all_product_lst,json_output_path)

csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\flipkart_computer\flipkart_new\flipkart_csv1.csv'
write_to_csv(all_product_lst, csv_output_path)

# dump_csv_to_database(csv_output_path)

# #
