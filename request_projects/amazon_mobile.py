import requests


from parsel import Selector

from functions.create_request import check_response, save_html

cookies = {
    'session-id': '262-4309065-9613011',
    'i18n-prefs': 'INR',
    'ubid-acbin': '258-8411464-9983951',
    'lc-acbin': 'en_IN',
    'session-id-time': '2082787201l',
    'csm-hit': 'tb:ZR74JP5J9QZ5F19CFKMH+s-05ME5VVDV0YYCX8SZ273|1750161236310&t:1750161236310&adb:adblk_no',
    'session-token': '3xMwJEmVz5R5XHSTULGwBAjkL9g+Wh4mXSXXeue6H965B0wHBLDZ9y9SZ/+Uh0zgjpzmfMXr26zL4FQpaIyxyx1fTAV5bzXnXojd//U22KjNTt5T4UosJBxJCWO9DPtvpVI1KtpXPa/kLAvHbtceDIdQunAXuWD+TnCZCqOJjyugI/JlsS4s1lWXRRI+vZfs6x32SDPO23ndwBP4jjnOwH34CYfC7OwYM7u6k1PaYHxC2nJ1KhjJZJRQNcL6rbywA86orVUllGyAuAt5X15lflH5s7m9PxRYIuG7zdhQngqb3jZ+048mfJ2UVAZsAqTzL0zj4HMlcekKiDgYicaZcYUmtMoVzZWQ',
    'rxc': 'AJnhePzKf7vAylcZJSU',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'device-memory': '8',
    'downlink': '7.55',
    'dpr': '1.1',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/s?k=mobile&crid=B1QG0WPJAGXZ&sprefix=mobile%2Caps%2C233&ref=nb_sb_noss_2',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.1',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-viewport-width': '1242',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'viewport-width': '1242',
    # 'cookie': 'session-id=262-4309065-9613011; i18n-prefs=INR; ubid-acbin=258-8411464-9983951; lc-acbin=en_IN; session-id-time=2082787201l; csm-hit=tb:ZR74JP5J9QZ5F19CFKMH+s-05ME5VVDV0YYCX8SZ273|1750161236310&t:1750161236310&adb:adblk_no; session-token=3xMwJEmVz5R5XHSTULGwBAjkL9g+Wh4mXSXXeue6H965B0wHBLDZ9y9SZ/+Uh0zgjpzmfMXr26zL4FQpaIyxyx1fTAV5bzXnXojd//U22KjNTt5T4UosJBxJCWO9DPtvpVI1KtpXPa/kLAvHbtceDIdQunAXuWD+TnCZCqOJjyugI/JlsS4s1lWXRRI+vZfs6x32SDPO23ndwBP4jjnOwH34CYfC7OwYM7u6k1PaYHxC2nJ1KhjJZJRQNcL6rbywA86orVUllGyAuAt5X15lflH5s7m9PxRYIuG7zdhQngqb3jZ+048mfJ2UVAZsAqTzL0zj4HMlcekKiDgYicaZcYUmtMoVzZWQ; rxc=AJnhePzKf7vAylcZJSU',
}

params = {
    'crid': '3KBGX7AQF9PIZ',
    'i': 'aps',
    'k': 'mobile',
    'ref': 'nb_sb_noss_2',
    'sprefix': 'mobile,aps,301',
    'url': 'search-alias=aps',
}

response = requests.get('https://www.amazon.in/s', params=params, cookies=cookies, headers=headers)
print(response.status_code)

my_response=check_response(response)
print(my_response)


html_path=r'C:\Users\Madri.Gadani\Desktop\madri\amazon_search\amazon_search_html.html'
my_html=save_html(response,html_path)

raw_html=response.text
# print(raw_html)

selector = Selector(text=raw_html)

product=selector.xpath('//div[@class="a-section"]')
print(len(product))

products = selector.xpath('//div[@data-component-type="s-search-result"]')
print("Number of products found:", len(products))

exit(0)
for i in product:
    name=i.xpath('//a[@class="a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"]//text()').get()
    print(name)

    name1 = i.xpath('.//a[@class="a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"]//text()').get()
    print(name1)



    price=i.xpath('//span[@class="a-price-whole"]/text()').get()
    print(price)
    mrp=i.xpath('//span[contains(text(),"M.R.P")]/text()').get()
    print(mrp)
    mrp2=i.xpath('//span[@data-a-color="secondary"]/span[@class="a-offscreen"]/text()').get()
    print(mrp2)
    total_reviews=i.xpath('//div[@class="a-row a-size-small"]//span[@class="a-size-base s-underline-text"]/text()').get()
    print(total_reviews)
    rating=i.xpath('//span[@class="a-declarative"]//span[@class="a-icon-alt"]/text()').get()
    print(rating)
    img_link=i.xpath('//div[@class="a-section aok-relative s-image-fixed-height"]//@src').get()
    print(img_link)
    product_link=i.xpath('//a[@class="a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"]/@href').get()

    product_link='https://www.amazon.in'+product_link
    print(product_link)
    print('///////////////////////////////////////////////////////////')

