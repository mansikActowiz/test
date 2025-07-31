import requests
import random
import gzip
from parsel import Selector
import json


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

    # Request headers
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

    output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_response_using_next_button.html'
    print(output_path)
    try:
        raw_html = response.text
        print(raw_html)
        # Write the HTML text as gzip-compressed file
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

        name=store.xpath('.//li[@class="outlet-name"]//text()').getall()
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

        print('//////////////////////////////////////////////')

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

def write_to_json(all_stored_data_lst,json_output_path):
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to {json_output_path}")
    

base_url = "https://stores.burgerking.in"
start_url = f"{base_url}/"

if __name__ == '__main__':
    all_stored_data_lst=[]
    current_url=start_url

    while True:
        print(f'Current url: {base_url}')

        response=create_request(current_url)

        if check_response(response):
            raw_html=save_html(response)
            if raw_html:
                page_data=parse(raw_html)
                all_stored_data_lst.extend(page_data)

            else:
                print('Failed to save HTML content')
        else:
            print('Response check failed. Skipping save and parse steps.')


        # Find the "Next" page URL
        selector = Selector(text=raw_html)
        next_page_relative = selector.xpath('//li[@class="next"]/a/@href').get()
            # '//ul[@class="pagination "]/li/a[contains(text(), "Next") and not(contains(@class, "disabled"))]/@href').get()

        if not next_page_relative:
            print("No more pages found.")
            break
        current_url = base_url+next_page_relative
        print(f'current_url:{current_url}')
    json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_data_using_next_button.json'
    write_to_json(all_stored_data_lst, json_output_path)




            ############################