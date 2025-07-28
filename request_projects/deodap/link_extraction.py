
import requests
import random
import gzip
from parsel import Selector
import os

url='https://deodap.in/'

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
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]
#
# def create_request(url):
#
#     headers = {
#         'User-Agent': random.choice(user_agents_lst),
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Connection': 'keep-alive',
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         print(f"Request Status: {response.status_code}")
#         return response
#     except Exception as e:
#         print(f"Error during request: {e}")
#         return None
#
#
# my_response=requests.get(url)
#
# print(my_response.status_code)
#
# def check_response(response):
#     if response and response.status_code == 200 :
#         return True
#     else:
#         return False
#
# my_check_response=check_response(my_response)
# print(my_check_response)
#
#
# raw_html=my_response.text
# # html_path = r'C:\Users\Madri.Gadani\Desktop\madri\deodap\deodap.html'
# # with open(html_path, 'w', encoding='utf-8') as file:
# #     file.write(raw_html)
# # print("HTML content fetched and written successfully.")
# #
# # with open(html_path, 'rb') as file_binary:
# #     with gzip.open(html_path + '.gz', 'wb') as file_gzip:
# #         file_gzip.writelines(file_binary)
# # print('file has been saved in compressed zip file.')
#
# selector=Selector(text=raw_html)
# link=selector.xpath('//a/@href').getall()
# # print(link)
# print(len(link))

url='https://deodap.in/'
sitemap_link=url+'robots.txt'
print(sitemap_link)

sitemap_response=requests.get(sitemap_link)
print(sitemap_response.status_code)

sitemap_html=sitemap_response.text
# print(sitemap_html)

sitemap_lst = [line.strip().split()[-1] for line in sitemap_html.splitlines() if line.strip().endswith('sitemap.xml')]
print(sitemap_lst)
sitemap_link=set(sitemap_lst)
print(sitemap_link)

prod_3=[]
all_links=[]
for i in sitemap_link:
    print(i)
    link_response=requests.get(i)
    link_html=link_response.text
    # print(link_html)

    selector=Selector(text=link_html)

    link_path=selector.xpath('//loc/text()').getall()
    print(link_path)

    for sep_link in link_path:
        print('///////////////////////////////////////')
        print('sep_link',sep_link)

        sep_link_response=requests.get(sep_link)
        print(sep_link_response.status_code)

        sep_link_html=sep_link_response.text
        print('######################################')
        # print('sep_link_html',sep_link_html)

        sep_link_selector=Selector(text=sep_link_html)
        individual_link=sep_link_selector.xpath('//loc/text()').getall()

        print(len(individual_link))
        individual_link=[link for link in individual_link if '/products' in link]
        # print(individual_link)

        print(len(individual_link))

        for j in individual_link:
            print(j) #https://deodap.in/products/9048-manual-sewing-roller-cutter-rotary-blade-1
            all_links.append(j)



            j_response=requests.get(j)
            print(j_response.status_code)
            j_html=j_response.text
            # print(j_html)


            individual_selector=Selector(text=j_html)

            # script_tag=individual_selector.xpath('/script/').getall()
            # print(script_tag)
            price=individual_selector.xpath('//span[@class="custom-price price-item price-item--sale price-item--last"]/text()').get()
            print(price)

            # img_link=individual_selector.xpath('//div[@class="test product__media media media--transparent"]//@src').get()
            # img_link='https:'+img_link
            # print(img_link)
            title=individual_selector.xpath('//title/text()').get()
            title=title.strip()

            print('title:',title)

            dict={
                'title':title,
                'price':price,
                # 'img_link':img_link,
            }
            print(dict)

print(all_links)
print(len(all_links))


