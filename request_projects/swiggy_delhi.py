import requests
import json
import time

cookies = {
    '__SW': 'UJX83ARt-iBlZL-DdDg04GbnWG_v8TYS',
    '_guest_tid': '27b8ec83-7838-46fa-ba27-0a09177bff61',
    '_device_id': '0ac8f23d-7404-5658-8e28-04a229564ef2',
    '_sid': 'kzla2724-3c86-4eb7-abdb-52ae5081e1b5',
}

headers = {
    '__fetch_req__': 'true',
    'accept': '*/*',
    'content-type': 'application/json',
    'referer': 'https://www.swiggy.com/restaurants',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}


lat = '28.6139'
lng = '77.2090'


# lat = '21.99740'
# lng = '79.00110'

restaurant_list = []
next_offset = None
page_number = 1

while True:
    if next_offset is None:
        # First request
        url = 'https://www.swiggy.com/dapi/restaurants/list/v5'
        params = {
            'lat': lat,
            'lng': lng,
            'is-seo-homepage-enabled': 'true',
            'page_type': 'DESKTOP_WEB_LISTING',
        }
    else:
        # Paginated request
        url = 'https://www.swiggy.com/dapi/restaurants/list/update'
        params = {
            'lat': lat,
            'lng': lng,
            'nextOffset': next_offset,
            'page_type': 'DESKTOP_WEB_LISTING',
        }

    print(f"\n🔄 Fetching page {page_number} ...")
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    if response.status_code != 200:
        print("❌ Failed to fetch data. Status Code:", response.status_code)
        break

    data = response.json()

    # Extract restaurants
    cards = data.get('data', {}).get('cards', [])
    found_restaurants = 0

    for card in cards:
        restaurants = (
            card.get('card', {})
            .get('card', {})
            .get('gridElements', {})
            .get('infoWithStyle', {})
            .get('restaurants', [])
        )
        for restaurant in restaurants:
            info = restaurant.get('info', {})
            name = info.get('name')
            link = restaurant.get('cta', {}).get('link', '')
            if name and link:
                restaurant_list.append((name, link))
                found_restaurants += 1

    print(f"✅ Page {page_number} — {found_restaurants} restaurants added.")

    # Get next offset
    next_offset = data.get('data', {}).get('pageOffset', {}).get('nextOffset')
    if not next_offset:
        print("\n✅ All pages fetched.")
        break

    page_number += 1
    time.sleep(1)  # Sleep to avoid overwhelming the server

# Print final list
print(f"\n📦 Total Restaurants Fetched: {len(restaurant_list)}\n")
for i, (name, link) in enumerate(restaurant_list, 1):
    print(f"{i}. {name} - {link}")
