import json
import gzip
from curl_cffi import requests
from parsel import Selector

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

#  Fetch HTML
main_page_response = requests.get(url, headers=headers, impersonate="chrome120")
raw_html = main_page_response.text

# Save HTML
output_path = r'C:\Users\Madri.Gadani\Desktop\madri\sankalp\sankalp_html.html'
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content written.")

# Compress HTML
with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('Compressed file saved.')

#  Parse country
main_page_select = Selector(text=raw_html)

country=main_page_select .xpath('//div[@class="jet-smart-filters-hierarchy jet-filter "]//select[@class="jet-select__control depth-0"]/option/text()').getall()
country_name=country[1:]
print(country_name)

countries_id= main_page_select.xpath('//div[@class="jet-smart-filters-hierarchy jet-filter "]//select[@class="jet-select__control depth-0"]/option/@value').getall()
main_countries_id=countries_id[1:]
print("Countries:", main_countries_id)

'''other method to get country id'''
# countries_id = main_page_select.xpath('//select[contains(@class, "depth-0")]//option/@value').getall()
# main_countries_id = [cid.strip() for cid in countries_id if cid.strip()]
# print("Countries:", main_countries_id)

# One country only
for country in main_countries_id:
    print(f"\nSelected Country: {country}")
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
    print(response_country.text)
    print('//////////////////////////////////')
    country_json = json.loads(response_country.text)
    print(country_json)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    state_html = country_json.get('data', {}).get('level_1', '')
    state_selector = Selector(text=state_html)
    state_ids = state_selector.xpath('//select[contains(@class, "depth-1")]//option/@value').getall()
    state_ids = [sid.strip() for sid in state_ids if sid.strip()]
    print("States:", state_ids)

    # One state only
    for state in state_ids:
        print(f"Selected State: {state}")
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
        state_json = json.loads(response_state.text)

        city_html = state_json.get('data', {}).get('level_1') or state_json.get('data', {}).get('level_2', '')
        city_selector = Selector(text=city_html)
        city_ids = city_selector.xpath('//select[contains(@class, "depth-2")]//option/@value').getall()
        city_ids = [cid.strip() for cid in city_ids if cid.strip()]
        print("Cities:", city_ids)

        # One city only
        for city in city_ids:
            print(f"Selected City: {city}")
            data = {
                'action': 'jet_smart_filters',
                'provider': 'jet-engine/default',
                'query[_tax_query_location]': city,
                'defaults[post_status][]': 'publish',
                'defaults[post_type]': 'restaurants',
                'defaults[posts_per_page]': '100',
                'defaults[paged]': '1',
                'defaults[ignore_sticky_posts]': '1',
                'defaults[date_query][0][column]': 'post_date',
                'defaults[date_query][0][after]': '',
                'defaults[date_query][0][before]': '',
                'settings[lisitng_id]': '1402',
                'settings[columns]': '3',
                'settings[columns_tablet]': '2',
                'settings[columns_mobile]': '1',
                'settings[column_min_width]': '240',
                'settings[column_min_width_tablet]': '',
                'settings[column_min_width_mobile]': '',
                'settings[inline_columns_css]': 'false',
                'settings[post_status][]': 'publish',
                'settings[use_random_posts_num]': '',
                'settings[posts_num]': '100',
                'settings[max_posts_num]': '13',
                'settings[not_found_message]': 'No data was found',
                'settings[is_masonry]': '',
                'settings[equal_columns_height]': '',
                'settings[use_load_more]': '',
                'settings[load_more_id]': 'loadMore',
                'settings[load_more_type]': 'click',
                'settings[load_more_offset][unit]': 'px',
                'settings[load_more_offset][size]': '0',
                'settings[loader_text]': '',
                'settings[loader_spinner]': '',
                'settings[use_custom_post_types]': '',
                'settings[custom_post_types]': '',
                'settings[hide_widget_if]': '',
                'settings[carousel_enabled]': '',
                'settings[slides_to_scroll]': '1',
                'settings[arrows]': 'true',
                'settings[arrow_icon]': 'fa fa-angle-left',
                'settings[dots]': '',
                'settings[autoplay]': 'true',
                'settings[pause_on_hover]': 'true',
                'settings[autoplay_speed]': '5000',
                'settings[infinite]': 'true',
                'settings[center_mode]': '',
                'settings[effect]': 'slide',
                'settings[speed]': '500',
                'settings[inject_alternative_items]': '',
                'settings[scroll_slider_enabled]': '',
                'settings[scroll_slider_on][]': [
                    'desktop',
                    'tablet',
                    'mobile',
                ],
                'settings[custom_query]': '',
                'settings[custom_query_id]': '',
                'settings[_element_id]': '',
                'settings[collapse_first_last_gap]': '',
                'settings[list_items_wrapper_tag]': 'div',
                'settings[list_item_tag]': 'div',
                'settings[empty_items_wrapper_tag]': 'div',
                'props[found_posts]': '1',
                'props[max_num_pages]': '1',
                'props[page]': '1',
            }

            response_city = requests.post('https://sankalprestaurants.com/wp-admin/admin-ajax.php',
                                     headers=headers, data=data)



            print(response_city.status_code)

            city_json = json.loads(response_city.text)
            content=city_json["content"]
            final_selector = Selector(text=content)
            stores = final_selector.xpath('//div[@data-post-id]')
            print(f"Found {len(stores)} stores.")

            for store in stores:
                content_fields = store.xpath('.//div[@class="jet-listing-dynamic-field__content"]/text()').getall()
                if len(content_fields) >= 2:
                    title = content_fields[0].strip()
                    address = content_fields[1].strip()
                    print(f" Title: {title}")
                    print(f" Address: {address}")
                    print("-" * 40)
                    exit()



            break

