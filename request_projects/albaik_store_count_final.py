import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine
import csv


url='https://www.al-baik.com/restaurants'

user_agents_lst = [
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
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

headers = {
    'User-Agent': random.choice(user_agents_lst),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}
try:
    response = requests.get(url, headers=headers)
    print(f"Request Status: {response.status_code}")
except Exception as e:
    print("no response found")

# output_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_store_locator\croma_response_html.html'
output_path=r'C:\Users\Madri.Gadani\Desktop\madri\albaik_store\albaik_store_all_html.html'
print(output_path)

raw_html=response.text
# print(raw_html)

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

selector = Selector(text=raw_html)
state_name=selector.xpath('//div[@class="col-md-3 d-md-block d-none"]/div[@class="list-group list-group-flush mb-md-4 mb-3"]//a/following-sibling::div')
state_lst=[]
state_count=[]
city_lst=[]
for state in state_name:
    state_=state.xpath(".//ancestor::div/preceding-sibling::a[1]/text()").get()
    city=state.xpath('.//a/text()').getall()
    count = len(city)
    print(state_)
    # print(city)
    print(count)
    state_lst.append(state_)
    state_count.append(count)
    city_lst.append(city)
print(state_lst)
print(state_count)
print(city_lst)
df=pd.DataFrame({
    'State':state_lst,
    'City':city_lst,
    'Count':state_count
})
df.to_csv(r'C:\Users\Madri.Gadani\Desktop\madri\albaik_store\albaik_store_state_vs_count1.csv',index=False)
print('csv has been created')
print(df)
exit(0)
