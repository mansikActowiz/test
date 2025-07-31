
import requests
import random
import gzip
from io import BytesIO
import xml.etree.ElementTree as ET
# import os
import re

from parsel import Selector

url='https://www.flipkart.com/robots.txt'
# url='https://www.flipkart.com'


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
        'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # Add more user agents if needed
    ]

headers = {
        'User-Agent': random.choice(user_agents_lst),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'}
response=requests.get(url,headers=headers)
print(response.status_code)

raw_html=response.text
# print(raw_html)

html_path=r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\flipkart_zip_extraction\html\sitemap.html'

with open(html_path,'w',encoding='UTF-8') as f:
        f.write(raw_html)
print('html file saved')

links = re.findall(r'http\S+?\.xml', raw_html)
print('links',len(links))



links_lst=[file for file in links if 'index' in file]
# print(links_lst)
print('links_lst',len(links_lst))

for cnt,i in enumerate(links_lst,start=1):
        print(i)
        safe_name=i.replace('.xml','')
        print(safe_name)

        index_response=requests.get(i,headers=headers)
        print(index_response.status_code)
        index_raw_html=index_response.text
        index_html_path=fr'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\flipkart_zip_extraction\index_html\index_{cnt}.html'
        with open (index_html_path,'w',encoding='UTF-8') as f:
                f.write(index_raw_html)
        print(f'index_raw_html for index {cnt} saved')

        print(index_raw_html)
        index_selector=Selector(text=index_raw_html)
        zip_link=index_selector.xpath('//loc/text()').getall()
        print('length of total zip_link',len(zip_link))

        for single_zip_link in zip_link:
                print(single_zip_link)

                zip_response=requests.get(single_zip_link,headers=headers)
                print(zip_response.status_code)
                zip_raw_html=zip_response.text

                compressed_file=BytesIO(zip_response.content)

                with gzip.GzipFile(fileobj=compressed_file, mode='rb') as f:
                        extracted_data = f.read().decode('utf-8')
                root = ET.fromstring(extracted_data)
                # print(root)
                namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

                # Step 4: Extract all product URLs from <loc> tags
                product_links = [elem.text for elem in root.findall('ns:url/ns:loc', namespace)]
                # print(product_links)
                print(len(product_links))

                for product in product_links:
                        print(product)
                        product_response=requests.get(product,headers=headers)
                        print(product_response.status_code)
                        product_raw_html=product_response.text
                        # print(product_raw_html)
                        product_selector=Selector(text=product_raw_html)
                        # product_name=product_selector.xpath('//div[@class="C7fEHH"]//h1//text()').get()
                        # print(product_name)
                        title = product_selector.css("title::text").get()
                        print("Title:", title)
                        exit(0)



                exit(0)



                # with open("sitemap_p_product_1.xml", "w", encoding='utf-8') as xml_file:
                #         xml_file.write(extracted_data)
                # print("Decompressed XML saved successfully.")





                exit(0)
                # # for cnt2,j in enumerate()
                # zip_html_path=r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\flipkart_zip_extraction\zip_html\'
                # with open(zip_html_path,'w',encoding='UTF-8') as f:
                #         f.write(zip_raw_html)
                #
                # exit(0)








