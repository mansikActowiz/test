import json
import time
from curl_cffi import requests
from parsel import Selector
import gzip
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://sankalprestaurants.com/south-indian-restaurant-near-me/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

url = 'https://sankalprestaurants.com/south-indian-restaurant-near-me/'
main_page_response = requests.get(url, headers=headers, impersonate="chrome120")

output_path = r'C:\Users\Madri.Gadani\Desktop\madri\sankalp\sankalp_html.html'
print(output_path)

raw_html=main_page_response.text


with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

print(url)

# selector = Selector(text=raw_html)


main_page_select = Selector(text=raw_html)

# Fix for country IDs
countries_id = main_page_select.xpath('//select[contains(@class, "depth-0")]//option/@value').getall()
main_countries_id = [cid for cid in countries_id if cid.strip()]  # remove empty entries
print("Countries:", main_countries_id)

for country in main_countries_id:
    data = {
        'action': 'jet_smart_filters_get_hierarchy_level',
        'filter_id': '1377',
        'values[0][value]': country,
        'values[0][tax]': 'location',
        'depth': '1',
        'args[show_label]': '',
        'args[display_options][show_items_label]': 'false',
        'args[display_options][show_decorator]': 'false',
        'args[display_options][filter_image_size]': 'full',
        'args[display_options][show_counter]': 'false',
    }

    response_country = requests.post('https://sankalprestaurants.com/wp-admin/admin-ajax.php', headers=headers, data=data, impersonate="chrome120")
    country_json = json.loads(response_country.text)

    getting_all_content = country_json.get('data', {}).get('level_1', '')
    country_selector = Selector(text=getting_all_content)
    state_id = country_selector.xpath('//select[contains(@class, "depth-1")]//option/@value').getall()
    main_state_id = [sid for sid in state_id if sid.strip()]
    print(f"\nCountry: {country} -> States: {main_state_id}")

    for state in main_state_id:
        data = {
            'action': 'jet_smart_filters_get_hierarchy_level',
            'filter_id': '1377',
            'values[0][value]': country,
            'values[0][tax]': 'location',
            'values[1][value]': state,
            'values[1][tax]': 'location',
            'depth': '2',
            'args[show_label]': '',
            'args[display_options][show_items_label]': 'false',
            'args[display_options][show_decorator]': 'false',
            'args[display_options][filter_image_size]': 'full',
            'args[display_options][show_counter]': 'false',
        }

        response_state = requests.post('https://sankalprestaurants.com/wp-admin/admin-ajax.php', headers=headers, data=data, impersonate="chrome120")
        my_state_json = json.loads(response_state.text)

        data_dict = my_state_json.get('data', {})
        getting_all_content_state = data_dict.get('level_1') or data_dict.get('level_2', '')

        if getting_all_content_state:
            my_selector_state = Selector(text=getting_all_content_state)
            city_id = my_selector_state.xpath('//select[contains(@class, "depth-2")]//option/@value').getall()
            city_id = [cid for cid in city_id if cid.strip()]
            print(f"State: {state} -> Cities: {city_id}")




            stores = my_selector_state.xpath('//div[@data-post-id]')  # Keep as selector list

            print(f"Found {len(stores)} stores.")

            for store in stores:
                content_fields = store.xpath('.//div[@class="jet-listing-dynamic-field__content"]/text()').getall()
                if len(content_fields) >= 2:
                    title = content_fields[0].strip()
                    address = content_fields[1].strip()
                    print(f"🏬 Title: {title}")
                    print(f"📍 Address: {address}")
                    print("-" * 40)
                    exit()





