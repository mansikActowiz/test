import json

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

#TODO:: For countries ID
url  = 'https://sankalprestaurants.com/south-indian-restaurant-near-me/'
main_page_r = requests.get(url, headers=headers, impersonate="chrome107")
main_page_select = Selector(text=main_page_r.text)

countries_id = main_page_select.xpath('//select[@class="jet-select__control depth-0"]//@value').getall()
print(countries_id)
main_countries_id=countries_id[1:]
print(main_countries_id)
# exit(0)
#TODO:: For states ID
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

    response = requests.post('https://sankalprestaurants.com/wp-admin/admin-ajax.php', headers=headers, data=data , impersonate="chrome120")

    my_json = json.loads(response.text)
    print(my_json)

    getting_all_content = my_json['data']['level_1']


    my_selector = Selector(text=getting_all_content)
    state_id = my_selector.xpath('//select[@class="jet-select__control depth-1"]//@value').getall()
    main_state_id=state_id[1:]
    print(main_state_id)


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
        response_state = requests.post('https://sankalprestaurants.com/wp-admin/admin-ajax.php',
                                 headers=headers, data=data,impersonate="chrome120")
        my_state_json = json.loads(response_state.text)

        try:
            getting_all_content_state = my_state_json.get('data',"").get('level_1',"")
            if not getting_all_content_state:
                getting_all_content_state = my_state_json.get('data', "").get('level_2', "")
            if not getting_all_content_state:
                getting_all_content_state = ''
        except Exception as e:
            print("Something went wrong")

        if getting_all_content_state:
            my_selector_state = Selector(text=getting_all_content_state)
            city_id = my_selector_state.xpath('//select[@class="jet-select__control depth-2"]//@value').getall()
            city_id=city_id[1:]
            print(city_id)

            response = requests.get(url, headers=headers)





            # exit(0)
            # # print(main_countries_id,'-',main_state_id,'-',city_id)
            # print('////////////////////////////////////////////////////')

