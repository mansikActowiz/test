import requests

from functions.create_request import check_response, save_html


import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.stayvista.com',
    'priority': 'u=1, i',
    'referer': 'https://www.stayvista.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'adults': 2,
    'children': 0,
    'city': 'goa',
    'state': 'goa',
    'filter_tags': [],
    'is_pax_selected': False,
    'max_bedrooms': 30,
    'min_bedrooms': 0,
    'page': 1,
    'price_end': 5000000,
    'price_start': 1000,
    'search_type': 'city',
    'total_guests': 2,
    'flex_window': 0,
    'pets_count': 0,
    'tax_inc': 0,
    'is_agent': 0,
}

response = requests.post('https://prod-searchapi.vistarooms.com/api/search/properties', headers=headers, json=json_data)


print(response.status_code)

check_response(response)


html_path = r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_1.html'

save_html(response,html_path)

data=response.json()
print(data)


hotels = data['properties']['secondary']
print('total no of hotels: ', len(hotels))

all_hotel_detail=[]

for hotel in hotels:
    try:

        checkin_date = data["extra_params"]["checkin"]
        checkout_date = data["extra_params"]["checkout"]
        no_of_pax = hotel['pricing']['min_occupancy']
        property_name = hotel['vista_name']
        location = hotel['city']
        slug = hotel['slug']
        link = f"https://www.stayvista.com/villa/{slug}" if slug else "N/A"
        price = hotel['pricing']['total_rental_cost']
        no_of_bedrooms = hotel['room']['number_of_rooms']
        meal=hotel['meal_type']
        # reviews=hotel['analytics']['rating']

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
        # print(f"Reviews        : {reviews}")


    except Exception as e:
        print(" Error while parsing hotel info:", e)

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
        # 'reviews': reviews,
    }
    all_hotel_detail.append(hotel_dict)

print(all_hotel_detail)


json_path=r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista_json.json'
# write_to_json(all_hotel_detail,json_path)

for index, hotel in enumerate(hotels, 1):
    name = hotel.get('vista_name', 'N/A')
    print(f"{index}. {name}")
