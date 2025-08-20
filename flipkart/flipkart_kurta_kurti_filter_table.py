
from urllib.parse import quote
from parsel import Selector
import mysql.connector
import requests
import json
import time
import random
from curl_cffi import requests


cookies = {
    'T': 'TI175463037559600185559379502332393567354467573374801932499086629278',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20309%7CMCMID%7C69546711188423189499195618647822413963%7CMCAAMLH-1755235148%7C12%7CMCAAMB-1755235148%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754637548s%7CNONE%7CMCAID%7CNONE',
    'vw': '1366',
    'dpr': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwODExNDIwMTQ3ODhQM0xLSEsiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDQxMzUyMSwiaWF0IjoxNzU0NjMzNTIxLCJqdGkiOiIxMjFlZTg1OS1jZjdmLTRjM2QtODk4OC0yMzUyZmYwYzEzNjUifQ.cE4WOweV-FpAHgC-MkfN2E_AsT6MDJuNEVmaOPx7Ybk',
    'ud': '7._EA8MPay8RgQCnXpsBXZHK5sc7gILo9FHj0aYgGHR1Oumr39zAo6t-7vuMSHXlmkUuxx5a6dthHiykOKVmj8-6JYMhAE-R64QEhI0aPsJh1tmTBdRrKHxyGGBvwc8qOhoUS2I2Momh6PF2Sb1hlfFy4n2wuS5aUifxkiWIztG_FDaKHAfmpyhrEN0l4YXrd1',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NTQ2NDY0MDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNDRjYTdhOTItZWExMC00NzA5LTg1MWYtMGRjMDYxYzhhN2IxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IjZKei0tRjl5ZHNzcl82bU5xc0JRa0x3VlNUUXktbkpaazlzandzdURVRzBXRVJVa2NGQ285QT09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YsA4hIT78xjyfM76wBtuVqaF248o9vjKmKY4EKC1_Pc',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzA1NDIyMDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNWI3ODIyZGItOGMzZi00NTFhLTkzN2EtYmFmNjlmNzQ4MWMxIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiS1hQRk1ZIn0.jQbJsjVpfS-Uq5psFGV7IN-qomGHeU3Cy8dEcxYEpXs',
    'K-ACTION': 'null',
    'vh': '607',
    'qH': '5985e3313e9e348f',
    'Network-Type': '3g',
    'vd': 'VI3B15274DB9524B47B106991AAB1770AC-1754630379676-4.1754646255.1754644605.151586550',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'S': 'd1t17Pz9VLT82fTF0URASP0QMaqC4cY3y61lcFfIXUG1iExF6OZtX06RaFs3wUQSztb/D93DQoDdAsRyXWVuVJ01hVg==',
    'SN': 'VI3B15274DB9524B47B106991AAB1770AC.TOK67B1C0DAE9A44B1CBA5210AF3BAAED43.1754646303581.LI',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version': '"138.0.7204.158"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.158", "Google Chrome";v="138.0.7204.158"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    # 'Cookie': 'T=TI175463037559600185559379502332393567354467573374801932499086629278; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20309%7CMCMID%7C69546711188423189499195618647822413963%7CMCAAMLH-1755235148%7C12%7CMCAAMB-1755235148%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754637548s%7CNONE%7CMCAID%7CNONE; vw=1366; dpr=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwODExNDIwMTQ3ODhQM0xLSEsiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDQxMzUyMSwiaWF0IjoxNzU0NjMzNTIxLCJqdGkiOiIxMjFlZTg1OS1jZjdmLTRjM2QtODk4OC0yMzUyZmYwYzEzNjUifQ.cE4WOweV-FpAHgC-MkfN2E_AsT6MDJuNEVmaOPx7Ybk; ud=7._EA8MPay8RgQCnXpsBXZHK5sc7gILo9FHj0aYgGHR1Oumr39zAo6t-7vuMSHXlmkUuxx5a6dthHiykOKVmj8-6JYMhAE-R64QEhI0aPsJh1tmTBdRrKHxyGGBvwc8qOhoUS2I2Momh6PF2Sb1hlfFy4n2wuS5aUifxkiWIztG_FDaKHAfmpyhrEN0l4YXrd1; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NTQ2NDY0MDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNDRjYTdhOTItZWExMC00NzA5LTg1MWYtMGRjMDYxYzhhN2IxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6IjZKei0tRjl5ZHNzcl82bU5xc0JRa0x3VlNUUXktbkpaazlzandzdURVRzBXRVJVa2NGQ285QT09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YsA4hIT78xjyfM76wBtuVqaF248o9vjKmKY4EKC1_Pc; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzA1NDIyMDUsImlhdCI6MTc1NDY0NDYwNSwiaXNzIjoia2V2bGFyIiwianRpIjoiNWI3ODIyZGItOGMzZi00NTFhLTkzN2EtYmFmNjlmNzQ4MWMxIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzU0NjMwMzc1NTk2MDAxODU1NTkzNzk1MDIzMzIzOTM1NjczNTQ0Njc1NzMzNzQ4MDE5MzI0OTkwODY2MjkyNzgiLCJiSWQiOiJLWFVYTFUiLCJrZXZJZCI6IlZJM0IxNTI3NERCOTUyNEI0N0IxMDY5OTFBQUIxNzcwQUMiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiS1hQRk1ZIn0.jQbJsjVpfS-Uq5psFGV7IN-qomGHeU3Cy8dEcxYEpXs; K-ACTION=null; vh=607; qH=5985e3313e9e348f; Network-Type=3g; vd=VI3B15274DB9524B47B106991AAB1770AC-1754630379676-4.1754646255.1754644605.151586550; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; S=d1t17Pz9VLT82fTF0URASP0QMaqC4cY3y61lcFfIXUG1iExF6OZtX06RaFs3wUQSztb/D93DQoDdAsRyXWVuVJ01hVg==; SN=VI3B15274DB9524B47B106991AAB1770AC.TOK67B1C0DAE9A44B1CBA5210AF3BAAED43.1754646303581.LI',
}

params = {
    'sid': 'clo,cfv,cib,rkt',
    'q': 'kurtas kurtis',
    'otracker': [
        'categorytree',
        'nmenu_sub_Women_0_Kurtas & Kurtis',
    ],
}




base_url='https://www.flipkart.com/clothing-and-accessories/ethnic-wear/kurtas/women-kurtas-and-kurtis/pr?sid=clo,cfv,cib,rkt&q=kurtas+kurtis&otracker=categorytree&otracker=nmenu_sub_Women_0_Kurtas%20%26%20Kurtis'



response = requests.get(base_url,
    params=params,
    cookies=cookies,
    impersonate="chrome110",
    headers=headers,
)
print(response.status_code)

# print(response.text)

time.sleep(random.uniform(1, 5))




sel = Selector(text=response.text)


script_data = sel.xpath('//script[contains(text(), "window.__INITIAL_STATE")]/text()').get()


script = script_data.replace('window.__INITIAL_STATE__ = ', '')[:-1]
data=json.loads(script)

brand_params_list = []

id=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][1]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[1].values[0].values[0].title'
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[1].title'
if id["title"] == "Brand":
    # print(id["values"])
    print('/////////////////////////////////////////////////////////')
    for value in id['values']:
        print(value)

        for val in value['values']:
            params_encoded = quote(val.get('resource').get('params'))
            print(params_encoded)
            brand_params_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Brand",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count":val.get('count'),

            })
print(brand_params_list)
print(len(brand_params_list)) #1417
# exit(0)

fabric_params_list=[]
fabric_list=[]
fabric=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][6]


if fabric['title'] == "fabric":
    for value in fabric['values']:
        for val in value['values']:
            fabric_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            fabric_params_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"fabric",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count":val.get('count'),

            })

print(len(fabric_params_list))  #15

kurta_type_list=[]
kurta_type_param_list=[]

kurta_type=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][11]

if kurta_type['title']=="Type":
    for value in kurta_type['values']:
        for val in value['values']:
            kurta_type_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))

            kurta_type_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"kurta Type",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

print(len(kurta_type_param_list))

pattern_list=[]
pattern_param_list=[]
pattern=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][5]

if pattern['title']=="Pattern":
    for value in pattern['values']:
        for val in value['values']:
            pattern_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            pattern_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Pattern",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })


print(len(pattern_param_list))

discount_param_list=[]
discount_list=[]
discount=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][3]

if discount['title']=="Discount":
    for value in discount['values']:
        for val in value['values']:
            discount_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            discount_param_list.append({
                 "category_name":"Kurta & Kurtia",
                "filter_type":"Discount",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

print(len(discount_param_list))

gender_param_list=[]
gender_list=[]
gender=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][2]

if gender['title']=="Gender":
    for value in gender['values']:
        for val in value['values']:
            gender_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            gender_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Gender",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
print(len(gender_param_list))


occasion_param_list=[]
occasion_list=[]
occasion=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][7]

if occasion['title']=="Occasion":
    for value in occasion['values']:
        for val in value['values']:
            occasion_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            occasion_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Occasion",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
print(len(occasion_param_list))

color_param_list=[]
color_list=[]
color=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][8]

if color['title']=="Color":
    for value in color['values']:
        for val in value['values']:
            color_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            color_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Color",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

print(len(color_param_list))


collection_list=[]
collection_param_list=[]
collection=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][14]

if collection['title']=="Collections":
    for value in collection['values']:
        for val in value['values']:
            collection_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            collection_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Collection",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

print(len(collection_param_list))


cutomer_rating_list=[]
cutomer_rating_param_list=[]
cutomer_rating=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][9]

if cutomer_rating['title']=="Customer Ratings":
    for value in cutomer_rating['values']:
        for val in value['values']:
            cutomer_rating_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            cutomer_rating_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Customer Ratings",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),
            })

print(len(cutomer_rating_param_list))



sleeve_list=[]
sleeve_param_list=[]
sleeve=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][13]

if sleeve['title']=="Sleeve Length":
    for value in sleeve['values']:
        for val in value['values']:
            sleeve_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            sleeve_param_list.append({
                 "category_name":"Kurta & Kurti",
                "filter_type":"Sleeve",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),


            })

print(len(sleeve_param_list))


arrival_list=[]
arrival_param_list=[]
arrival=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][15]

if arrival['title']=="New Arrivals":
    for value in arrival['values']:
        for val in value['values']:
            arrival_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            arrival_param_list.append({
                "category_name":"Kurta & Kurti",
                "filter_type":"New Arrivals",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
print(len(arrival_param_list))



combined_list=[]
combined_list.extend(brand_params_list)
combined_list.extend(fabric_params_list)
combined_list.extend(kurta_type_param_list)
combined_list.extend(pattern_param_list)
combined_list.extend(gender_param_list)
combined_list.extend(occasion_param_list)
combined_list.extend(color_param_list)
combined_list.extend(collection_param_list)
combined_list.extend(arrival_param_list)
combined_list.extend(cutomer_rating_param_list)
combined_list.extend(sleeve_param_list)
combined_list.extend(discount_param_list)
print(len(combined_list))



# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',       # change if needed
    user='root',   # change to your MySQL username
    password='Actowiz', # change to your MySQL password
    database='flipkart_kurta_kurti'  # change to your database name
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS flipkart_kurta_kurti_filters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255),
    filter_type VARCHAR(255),
    filter_name VARCHAR(255),
    slug TEXT,
    url TEXT,
    count TEXT,
    total_count TEXT,
    status TEXT
)
''')

# Insert each row
for row in combined_list:
    cursor.execute('''
        INSERT INTO flipkart_kurta_kurti_filters (category_name, filter_type, filter_name, slug, url, count, total_count, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        row['category_name'],
        row['filter_type'],
        row['filter_name'],
        row['slug'],
        row['url'],
        row['count'],
        0,
        'pending'
    ))

conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL table successfully.")


