import requests
import gzip
import json
import csv
import pandas as pd
from sqlalchemy import create_engine

from parsel import Selector


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





cookies = {
    '__SW': 'UJX83ARt-iBlZL-DdDg04GbnWG_v8TYS',
    '_guest_tid': '27b8ec83-7838-46fa-ba27-0a09177bff61',
    '_device_id': '0ac8f23d-7404-5658-8e28-04a229564ef2',
    '_sid': 'kzla2724-3c86-4eb7-abdb-52ae5081e1b5',
    'userLocation': '{%22lat%22:%2221.99740%22%2C%22lng%22:%2279.00110%22%2C%22address%22:%22%22%2C%22area%22:%22%22%2C%22showUserDefaultAddressHint%22:false}',
    'fontsLoaded': '1',
    '_gcl_au': '1.1.375715284.1749094806',
    '_gid': 'GA1.2.1363117266.1749094807',
    '_ga_YE38MFJRBZ': 'GS2.1.s1749094806$o1$g1$t1749095940$j60$l0$h0',
    '_ga_34JYJ0BCRN': 'GS2.1.s1749094806$o1$g1$t1749095940$j60$l0$h0',
    '_ga': 'GA1.2.1264974629.1749094807',
    '_gat_0': '1',
}

headers = {
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'if-none-match': 'W/"11cb5-ied6h2KSv7snWajz1znLuvGPO24"',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/restaurants',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': '__SW=UJX83ARt-iBlZL-DdDg04GbnWG_v8TYS; _guest_tid=27b8ec83-7838-46fa-ba27-0a09177bff61; _device_id=0ac8f23d-7404-5658-8e28-04a229564ef2; _sid=kzla2724-3c86-4eb7-abdb-52ae5081e1b5; userLocation={%22lat%22:%2221.99740%22%2C%22lng%22:%2279.00110%22%2C%22address%22:%22%22%2C%22area%22:%22%22%2C%22showUserDefaultAddressHint%22:false}; fontsLoaded=1; _gcl_au=1.1.375715284.1749094806; _gid=GA1.2.1363117266.1749094807; _ga_YE38MFJRBZ=GS2.1.s1749094806$o1$g1$t1749095940$j60$l0$h0; _ga_34JYJ0BCRN=GS2.1.s1749094806$o1$g1$t1749095940$j60$l0$h0; _ga=GA1.2.1264974629.1749094807; _gat_0=1',
}

params = {
    'lat': '21.99740',
    'lng': '79.00110',
    'is-seo-homepage-enabled': 'true',
    'page_type': 'DESKTOP_WEB_LISTING',
}

url='https://www.swiggy.com/dapi/restaurants/list/v5'

response = requests.get(url,params=params, cookies=cookies, headers=headers)
print(response.status_code)
print(response.text)


raw_html=response.text

output_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_html1.html'



with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

print(url)

json_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_raw_try.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(response.json(), json_file, indent=4, ensure_ascii=False)
print(f"JSON content saved to {json_path}")
json_path = r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_raw.json'

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
            name = info.get('name')
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
    print(f"Cuisines: {r['cuisines']}")
    print(f"  Rating: {r['rating']}")
    print(f" Delivery Time: {r['delivery_time']}")
    print(f"  {r['cost_for_two']}")
    print(f"  Link: {r['link']}\n")



csv_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\swiggy\swiggy_csv.csv'
col_names=['name','link','rating','cuisines','delivery_time','cost_for_two']

# write_to_csv(restaurant_list,csv_output_path)
dump_csv_to_sql(csv_output_path,'swiggy','swiggy_table')
