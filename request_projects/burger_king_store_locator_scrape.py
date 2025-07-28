import requests
import random
import gzip
from parsel import Selector
import json

def create_request():

    url = "https://stores.burgerking.in/location/gujarat/ahmedabad"

    # List of user agents to randomly pick one (to mimic real browser requests)
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

    # Request headers
    headers = {
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }


    output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_response.html'
    print(output_path)

    try:
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
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
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def parse(html_page):
    selector = Selector(text=html_page)
    stores = selector.xpath('//div[@class="store-info-box"]')
    print('stores',len(stores))


    store_data=[]

    for store in stores:

        name=store.xpath('.//li[@class="outlet-name"]//text()').getall()
        store_name = next((x.strip() for x in name if x.strip()), None)
        print('Store name:',store_name)

        add=store.xpath('.//li[@class="outlet-address"]//text()').getall()
        cleaned_address = [line.strip() for line in add if line.strip() != '']
        store_address=','.join(cleaned_address)
        print('store_address',store_address)

        phone=store.xpath('.//li[@class="outlet-phone"]//text()').getall()
        phone = next((x.strip() for x in phone if x.strip()), None)
        print('Contact number:',phone)

        map=store.xpath('.//a[@class="btn btn-map"]/@href').getall()[0]
        print('Map link',map)

        website=store.xpath('.//a[@class="btn btn-website"]/@href').getall()[0]
        print('website link',website)

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
    json_output_path = r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\store_locator_data.json'
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump(store_data, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to {json_output_path}")

    


if __name__ == '__main__':
    html_page = create_request()
    if html_page:
        parse(html_page)
    else:
        print('No response to parse.')

