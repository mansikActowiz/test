import requests
import gzip

from parsel import Selector

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://order.pacificcatch.com/order?branchId=5ecb830e6212ff0e3a164aa1&branchName=Campbell&search=&servingOptionType=pickup/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
}

response = requests.get(
    'https://order.pacificcatch.com/page-data/order/page-data.json?branchId=5ecb830e6212ff0e3a164aa1&branchName=Campbell&search=&servingOptionType=pickup/',
    headers=headers,
)
print(response.status_code)

raw_html=response.text
print(raw_html)

output_path=r'C:\Users\Madri.Gadani\Desktop\madri\google_place_API\pacific\html\pacific.html'

gzip_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\google_place_API\pacific\html\pacific_gzip.html'


with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')

selector=Selector(text=raw_html)

import json
data=response.json()
# print(data)
print(json.dumps(data, indent=4))
menu_items = data['result']['pageContext']['menuData'][1]['items']
# 0.result.pageContext.menuData[31].items[0].name
print(menu_items)
for item in menu_items:
    print(item['name'])

    'AIzaSyCFF3MgmVjgeFyrh7aHGFnAE8MJnAIK-WI'
