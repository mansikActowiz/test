import requests
import gzip
import json
import csv
import pandas as pd
from sqlalchemy import create_engine

from parsel import Selector

from database_programs.database_functions import create_mysql_database


def write_to_csv(restaurant_list,csv_output_path):
    with open(csv_output_path, 'w', encoding='utf-8') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(restaurant_list)
    print(f"Data saved to CSV path:{csv_output_path}")

def dump_csv_to_sql(csv_output_path,database_name,database_table_name):

    df = pd.read_csv(csv_output_path)
    print(df)
    user = 'root'
    password = 'Actowiz'  # e.g., 'Actowiz'
    host = 'localhost'
    database = database_name#'swiggy'  # <-- your correct DB name

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    # Create table if not exists and insert data
    df.to_sql(database_table_name, con=engine, if_exists='replace', index=False) #swiggy_table

    print(f"Data inserted successfully into table  {database_table_name} in {database_name} database.")





import requests

cookies = {
    '__SW': 'UJX83ARt-iBlZL-DdDg04GbnWG_v8TYS',
    '_guest_tid': '27b8ec83-7838-46fa-ba27-0a09177bff61',
    '_device_id': '0ac8f23d-7404-5658-8e28-04a229564ef2',
    '_sid': 'kzla2724-3c86-4eb7-abdb-52ae5081e1b5',
    'fontsLoaded': '1',
    '_gcl_au': '1.1.375715284.1749094806',
    '_gid': 'GA1.2.1363117266.1749094807',
    '_ga': 'GA1.2.1264974629.1749094807',
    '_gat_0': '1',
    'userLocation': '{%22address%22:%22Ahmedabad%2C%20Gujarat%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:23.022505%2C%22lng%22:72.5713621}',
    'dadl': 'true',
    '_ga_34JYJ0BCRN': 'GS2.1.s1749103485$o3$g1$t1749104535$j2$l0$h0',
    '_ga_YE38MFJRBZ': 'GS2.1.s1749103485$o3$g1$t1749104535$j2$l0$h0',
}

headers = {
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.swiggy.com',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/restaurants',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': '__SW=UJX83ARt-iBlZL-DdDg04GbnWG_v8TYS; _guest_tid=27b8ec83-7838-46fa-ba27-0a09177bff61; _device_id=0ac8f23d-7404-5658-8e28-04a229564ef2; _sid=kzla2724-3c86-4eb7-abdb-52ae5081e1b5; fontsLoaded=1; _gcl_au=1.1.375715284.1749094806; _gid=GA1.2.1363117266.1749094807; _ga=GA1.2.1264974629.1749094807; _gat_0=1; userLocation={%22address%22:%22Ahmedabad%2C%20Gujarat%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:23.022505%2C%22lng%22:72.5713621}; dadl=true; _ga_34JYJ0BCRN=GS2.1.s1749103485$o3$g1$t1749104535$j2$l0$h0; _ga_YE38MFJRBZ=GS2.1.s1749103485$o3$g1$t1749104535$j2$l0$h0',
}

json_data = {
    'lat': 23.022505,
    'lng': 72.5713621,
    'nextOffset': 'CJhlELQ4KIDg2qqP76XaUDCnEzgC',
    'widgetOffset': {
        'NewListingView_category_bar_chicletranking_TwoRows': '',
        'NewListingView_category_bar_chicletranking_TwoRows_Rendition': '',
        'Restaurant_Group_WebView_SEO_PB_Theme': '',
        'collectionV5RestaurantListWidget_SimRestoRelevance_food_seo': '9',
        'inlineFacetFilter': '',
        'restaurantCountWidget': '',
    },
    'filters': {},
    'seoParams': {
        'seoUrl': 'https://www.swiggy.com/restaurants',
        'pageType': 'FOOD_HOMEPAGE',
        'apiName': 'FoodHomePage',
        'businessLine': 'FOOD',
    },
    'page_type': 'DESKTOP_WEB_LISTING',
    '_csrf': 'hNQCygf2hB5i-Ri5nIJdk5g6fl2wEjYzrDdNr53I',
}

response = requests.post('https://www.swiggy.com/dapi/restaurants/list/update', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"lat":23.022505,"lng":72.5713621,"nextOffset":"CJhlELQ4KIDg2qqP76XaUDCnEzgC","widgetOffset":{"NewListingView_category_bar_chicletranking_TwoRows":"","NewListingView_category_bar_chicletranking_TwoRows_Rendition":"","Restaurant_Group_WebView_SEO_PB_Theme":"","collectionV5RestaurantListWidget_SimRestoRelevance_food_seo":"9","inlineFacetFilter":"","restaurantCountWidget":""},"filters":{},"seoParams":{"seoUrl":"https://www.swiggy.com/restaurants","pageType":"FOOD_HOMEPAGE","apiName":"FoodHomePage","businessLine":"FOOD"},"page_type":"DESKTOP_WEB_LISTING","_csrf":"hNQCygf2hB5i-Ri5nIJdk5g6fl2wEjYzrDdNr53I"}'
#response = requests.post('https://www.swiggy.com/dapi/restaurants/list/update', cookies=cookies, headers=headers, data=data)
url='https://www.swiggy.com/dapi/restaurants/list/update'

# response = requests.get(url, cookies=cookies, headers=headers)
print(response.status_code)
print(response.text)


raw_html=response.text

output_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_html2.html'



with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

print(url)

json_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_raw_try2.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(response.json(), json_file, indent=4, ensure_ascii=False)
print(f"JSON content saved to {json_path}")
json_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_raw_try2.json'

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data.keys())

cards = data.get('data', {}).get('cards', [])
print(cards)

# Find the card that contains restaurants


restaurant_list = []
for card in cards:
    grid = card.get('card', {}).get('card', {}).get('gridElements', {})
    if 'infoWithStyle' in grid:
        restaurants = grid['infoWithStyle'].get('restaurants', [])
        for restaurant in restaurants:
            info = restaurant.get('info', {})
            id=info.get('id')
            name = info.get('name')
            locality=info.get('locality')
            area=info.get("areaName")
            link = restaurant.get('cta', {}).get('link')  # 'cta' contains the restaurant URL path
            rating = info.get('avgRating')
            cuisines = ", ".join(info.get('cuisines', []))
            delivery_time = info.get('sla', {}).get('slaString')
            cost_for_two = info.get('costForTwo')
            if name and link:
                full_link = f"{link}"
                restaurant_list.append({
                    'name': name,
                    'link': full_link,
                    'locality' :locality,
                    'area': area,
                    'rating': rating,
                    'cuisines': cuisines,
                    'delivery_time': delivery_time,
                    'cost_for_two': cost_for_two,

                })

print(restaurant_list)



# Print restaurant names and their links
print("\nList of Restaurants:")
for i, r in enumerate(restaurant_list, 1):

    print(f"{i}. {r['name']}")
    print(f"link: {r['link']}")
    print(f"locality: {r['locality']}")
    print(f"area: {r['area']}")
    print(f"Cuisines: {r['cuisines']}")
    print(f"  Rating: {r['rating']}")
    print(f" Delivery Time: {r['delivery_time']}")
    print(f"  {r['cost_for_two']}")
    print(f"  Link: {r['link']}\n")

# exit(0)

csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_csv_abad.csv'
col_names=['name','link','locality','area','rating','cuisines','delivery_time','cost_for_two']

# write_to_csv(restaurant_list,csv_output_path)
# create_mysql_database('swiggy_ahmedabad')

dump_csv_to_sql(csv_output_path,'swiggy_ahmedabad','swiggy_ahmedabad_table')
