import requests
import random
import gzip
import json
from parsel import Selector


BASE_URL = 'https://store.croma.com/'
MASTER_OUTLET_ID = 247436
USER_AGENTS = [
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]


def create_request(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Request to {url} | Status: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def check_response(response):
    return response is not None and response.status_code == 200

def fetch_html(url):
    response = create_request(url)
    if check_response(response):
        html_text=response.text
        return html_text
    return None



def save_html_compressed(html_text, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_text)
    with open(path, 'rb') as fb, gzip.open(path + '.gz', 'wb') as fgz:
        fgz.writelines(fb)
    print(f"Saved and compressed HTML to {path}.gz")


def get_states(selector):
    states = selector.xpath('//select[@name="stateName"]/option/@value').getall()
    return [s for s in states if s]




def get_cities_by_state(state):
    url = f'{BASE_URL}getCitiesByMasterOutletIdAndStateName.php?master_outlet_id={MASTER_OUTLET_ID}&state_name={state}'
    response = create_request(url)
    if check_response(response):
        return json.loads(response.text)
    return {}

def get_localities_by_city(city):
    url = f'{BASE_URL}getLocalitiesByMasterOutletIdAndCityName.php?master_outlet_id={MASTER_OUTLET_ID}&city_name={city}'
    response = create_request(url)
    if check_response(response):
        return json.loads(response.text)
    return {}


def extract_store_data(html_text):
    selector = Selector(text=html_text)
    stores = selector.xpath('//div[@class="store-info-box"]')
    print(f"Found {len(stores)} stores")
    data = []
    for store in stores:
        name = ','.join([n.strip() for n in store.xpath('.//div[@class="info-text"]/a[@href]/text()').getall() if n.strip()])
        address = ','.join([a.strip() for a in store.xpath('.//li[@class="outlet-address"]/div[@class="info-text"]//text()').getall() if a.strip()])
        phone = store.xpath('.//li[@class="outlet-phone"]//text()').getall()
        store_phone = [p.strip() for p in phone if p.strip()][0]
        timing =store.xpath('.//li[@class="outlet-timings"]//text()').getall()
        store_timing = [t.strip() for t in timing if t.strip()][0]

        data.append({
            'store_name': name,
            'store_address': address,
            'store_phone': store_phone,
            'store_timing': store_timing,
        })
    return data


def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to JSON at {path}")


def main():
    base_html = fetch_html(BASE_URL)
    if not base_html:
        return

    html_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\croma_response_html_27.html'
    save_html_compressed(base_html, html_path)

    selector = Selector(text=base_html)
    states = get_states(selector)
    print(f"States: {states}")

    all_data = []
    for state in states:
        cities = get_cities_by_state(state)
        for city in cities.keys():
            localities = get_localities_by_city(city)
            for locality in localities.keys():
                store_url = f'{BASE_URL}location/{state}/{city}/{locality}'
                store_html = fetch_html(store_url)
                if not store_html:
                    continue

                final_html_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\final_croma_response_html_new_27.html'
                save_html_compressed(store_html, final_html_path)

                store_data = extract_store_data(store_html)
                all_data.extend(store_data)

    json_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\final_croma_response_json_new_27.json'
    save_json(all_data, json_path)


if __name__ == "__main__":
    main()
