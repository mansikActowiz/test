import requests
import random
import gzip
import os
from parsel import Selector


def make_request():
    # URL of the Burger King stores page
    url = "https://stores.burgerking.in/location/gujarat/ahmedabad"

    # Add headers to mimic a browser request
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
    ]
    headers = {
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    try:
        if os.path.exists(r'D:\Dev\WizStack\Retail-Fs\BKStores\response.html.gz'):
            print('The path exist..')
            with gzip.open(r'D:\Dev\WizStack\Retail-Fs\BKStores\response.html.gz', 'rb') as file:
                html = file.read()
            return str(html)

        else:
            # Make request
            response = requests.get(url, headers=headers)
            # Save the HTML content to a file
            with gzip.open(r'C:\Users\Madri.Gadani\Desktop\madri\store_locator\response.html.gz', 'wb') as file:
                file.write(response.content)
            return None

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def parse(html_page):
    selector = Selector(text=html_page)
    data = {}
    data['store_name'] = selector.xpath('//div[@class="store-info-box"]//li[@class="outlet-name"]//text()').get()
    print(data)
    return data

if __name__ == '__main__':
    html_page = make_request()
    if html_page:
        parse(html_page)
    else:
        print('No response')

