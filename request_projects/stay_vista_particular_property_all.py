from functions.create_json_file import write_to_json
from functions.create_request import check_response, save_html, get_or_save_html
import os
import json
import csv
import gzip
import random
from parsel import Selector
import pandas as pd

import requests

url_lst= [
        'https://www.stayvista.com/villa/casa-armeh?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-canto?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-ti-amo?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/sapphire-sands?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-vida?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-del-lusso?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/villa-magnifica?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/a-portuguese-tale?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-saipem?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/brew-breeze?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
        'https://www.stayvista.com/villa/casa-san-antonio?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true',
    ]
# url='https://www.stayvista.com/villa/casa-armeh?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true'
# url='https://www.stayvista.com/villa/casa-canto?checkin=2025-06-25&checkout=2025-06-26&rooms_booked=4&same_date=true'

all_data=[]

for i in url_lst:
    print(i)
    slug = i.split("/villa/")[1].split("?")[0]
    print(slug)
    # exit(0)

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
        response = requests.get(i, headers=headers)
        print(f"Request Status: {response.status_code}")
    except Exception as e:
        print("no response found")

    print(response.status_code)

    '''call the check_response function to check the response'''
    check_response(response)

    '''call the get_or_save_html function to create html '''
    html_path = fr'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_particular_urls_only\stay_vista_casa_{slug}.html'

    raw_html=response.text


    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(raw_html)
    print("HTML content fetched and written successfully.")

    with open(html_path, 'rb') as file_binary:
        with gzip.open(html_path + '.gz', 'wb') as file_gzip:
            file_gzip.writelines(file_binary)
    print('file has been saved in compressed zip file.')
    print('///////////////////////////////////////////')


    selector = Selector(text=raw_html)
    json_text = selector.xpath('//script[@id="__NEXT_DATA__"]/text()').get()


    if json_text:
        data = json.loads(json_text)


        checkin_date=data['query']['checkin']
        checkout_date=data['query']['checkout']
        no_of_pax=data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['min_occupancy']
        property_name = data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['vista_name']
        location = data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['city']
        slug = data['props']['pageProps']['slug']
        link = f"https://www.stayvista.com/villa/{slug}" if slug else "N/A"
        no_of_bedrooms = data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['number_of_rooms']
        meal = 'Available'
        reviews = data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['ratings']
        property_id=data['props']['pageProps']['propertyDetailsObj']['data']['property_detail']['id']
        print('property_id',property_id)

        headers = {
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authorization': 'Bearer',
            'content-type': 'application/json',
            'origin': 'https://www.stayvista.com',
            'priority': 'u=1, i',
            'referer': 'https://www.stayvista.com/',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        }

        json_data = {
            'property_id':property_id,
            'checkin': '2025-06-25',
            'checkout': '2025-06-26',
            'adult': 2,
            'child': 0,
            'infant': 0,
            'rooms_booked': 4,
            'guest': 2,
            'package_type': '',
            'credit_note': '',
            'coupon_code': '',
            'bank_offer_code': '',
            'check_availability': 0,
        }

        response2 = requests.post('https://v3api.stayvista.com/api/price-breakup', headers=headers, json=json_data)
        print(response2.status_code)
        data2 = response2.json()
        print(json.dumps(data2, indent=4))
        price = data2['data']['price']['total_rental_cost']


        print("=" * 60)
        print(f"Check-in Date   : {checkin_date}")
        print(f"Check-out Date  : {checkout_date}")
        print(f"No. of PAX      : {no_of_pax}")
        print(f"Property Name   : {property_name}")
        print(f"Location        : {location}")
        print(f"Link            : {link}")
        print(f"Price           : ₹{price}")
        print(f"No. of Bedrooms : {no_of_bedrooms}")
        print(f"Meals Included   : {meal}")
        print(f"Reviews        : {reviews}")

        hotel_dict = {
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'no_of_pax': no_of_pax,
            'property_name': property_name,
            'location': location,
            'link': link,
            'price': price,
            'no_of_bedrooms': no_of_bedrooms,
            'meal': meal,
            'reviews': reviews,
        }
        print(hotel_dict)

        all_data.append(hotel_dict)
print(all_data)

json_path=r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_particular_urls_only\all_json.json'

write_to_json(all_data,json_path)


csv_path=r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_particular_urls_only\stay_vista_particular_url_final_csv.csv'
# csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_particular_urls_only\stay_vista_particular_url_csv1.csv'

df=pd.read_json(json_path)
df.to_csv(csv_path,index=False)
