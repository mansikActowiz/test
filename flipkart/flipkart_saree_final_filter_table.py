
from urllib.parse import quote
from parsel import Selector
import requests
import mysql.connector

cookies = {
    'Network-Type': '4g',
    'T': 'TI174824499597300142754598348542330031370306090257579454047282066136',
    'vw': '1366',
    'dpr': '1',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20305%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754896184%7C12%7CMCAAMB-1754896184%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754298584s%7CNONE%7CMCAID%7CNONE',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwNDEzMDY0MTM0NlhZMVFQQjQiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDA3MzAwMSwiaWF0IjoxNzU0MjkzMDAxLCJqdGkiOiJmNjkxNjlkMS1iZjQ4LTQyYmUtYTZmNy02YTQwMjNkZDJhYTUifQ.SKmnWwLkb78ePUma4KSDEwCPfi3poN8hGsdKbBCJDaU',
    'ud': '1.3RovXtHZlV6Ku4MnxYAGp12z9rswmi-Rm7GUyv5aizXCUI2_V6rn93V7V4ogfQ4fm36i3_Z-aKTDlXSoF8wff_IQZNwjcoc8StHK3heQPEGKiQ7fD2YXEJAqNIjdvPbYIcP0uyVQK_Y7JMx2MsbJpX0PzkH-h809MqE7h0TzhCgNLPAU3b7cXPjoKOGrtttm',
    'qH': '3a4bc565a4835306',
    'vh': '607',
    'K-ACTION': 'null',
    'Network-Type': '4g',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aclothing-and-accessories%25253Asaree-and-accessories%25253Asaree%25253Awomen-saree%25253Apr%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DLABEL',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NTQzOTgwODYsImlhdCI6MTc1NDM5NjI4NiwiaXNzIjoia2V2bGFyIiwianRpIjoiNzgxMWI4NDMtM2E0My00ODc5LThlOTctZTA0YzVkM2U0YWFjIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJOUENDSU4iLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6Ikh1dnp3VVJfMjNfMEVWaEdZVzFudzVlblptUG9DZ2pzaURXcE5iSGpqeFpoZWpBZGNRUm9wZz09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.YaY9t4-OlWKS9ZN8BtWgFO1ssH97B0ANI7aYxD1kLQ8',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3NzAyOTM4ODYsImlhdCI6MTc1NDM5NjI4NiwiaXNzIjoia2V2bGFyIiwianRpIjoiY2Y2MzE2YWQtZDE2Yy00NWYzLWFlM2EtNTAzNDBmNjMxY2IzIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJOUENDSU4iLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiUkg0QzJFIn0.1LwkTCgg0xnEzp62754Ou8LhMInCGtKhzPeEXaqF8LA',
    'S': 'd1t16Pz8/cz97Pwk/Pz8/PzRHP0yCWGrNF/yaaYkSbMiPDJQ9EEX37c4ffSMcEeC70phHEgCX+bg90yYET3VrOBMh1g==',
    'vd': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872-1754284011313-7.1754396726.1754391734.158529491',
    'SN': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK37FC9F697D514E74885B72C818ADD1EF.1754396742543.LI',
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
    # 'Cookie': 'Network-Type=4g; T=TI174824499597300142754598348542330031370306090257579454047282066136; rt=null; K-ACTION=null; ud=7._EA8MPay8RgQCnXpsBXZHDhEvrPi_FigMKvNKmSmvPkYNsXpjGM3sYBdoc3UdkrlNyE0WjSJs9YHBeCXrvRRnRlm3F8DwKy2yKyTzWwt15btu3Dh9NCHLAZB5HSBDMKK9HnDy5_h6L6yK5COVaD2Aw; vw=1366; dpr=1; vh=641; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3NTU0MTI4ODAsImlhdCI6MTc1MzY4NDg4MCwiaXNzIjoia2V2bGFyIiwianRpIjoiMTBmODRlN2MtYjYwZC00NTQxLTgzYjAtNGQ4MTc2YWQyODYzIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.uRkVBGj_YPFHtMKQyqsrWf5wigFoikhZTAV7iCMaCvs; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; Network-Type=4g; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20302%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754289652%7C12%7CMCAAMB-1754622877%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754025277s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; vd=VI5FAAFE7DD4B443C198E5E65ACCA7C872-1748244997568-25.1754020985.1754017754.163439705; S=d1t16Pz9MTj99Pz9PPz8fST8EP+ZO54wrqFnBw3mVTQCDooFGHj1V8d2pOFcOKwttS5AMtjbVJn26GLESZCo9m7jLjA==; SN=VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOKDB4F35E4133A4C6084AACB725B67E80F.1754020985965.LO',
}
url_brand='https://www.flipkart.com/clothing-and-accessories/saree-and-accessories/saree/women-saree/pr?sid=clo,8on,zpd,9og&otracker=categorytree&otracker=nmenu_sub_Women_0_Sarees'

base_url='https://www.flipkart.com/clothing-and-accessories/saree-and-accessories/saree/women-saree/pr?sid=clo%2C8on%2Czpd%2C9og&otracker=categorytree&otracker=nmenu_sub_Women_0_Sarees'

response = requests.get(url_brand,
    cookies=cookies,
    headers=headers,
)


import json
response_brand = requests.get(url_brand, headers=headers)
sel = Selector(text=response_brand.text)






script_data = sel.xpath('//script[contains(text(), "window.__INITIAL_STATE")]/text()').get()

script = script_data.replace('window.__INITIAL_STATE__ = ', '')[:-1]

data=json.loads(script)


brand_list = list()
brand_params_list = []
title=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][1]['values'][0]['values'][0]['title']
id=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][1]

if id["title"] == "Brand":
    for value in id['values']:
        for val in value['values']:
            params_encoded = quote(val.get('resource').get('params'))
            brand_params_list.append({
                 "category_name":"Sarees",
                "filter_type":"Brand",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })



fabric_params_list=[]
fabric_list=[]
fabric=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][6]

if fabric['title'] == "fabric":
    for value in fabric['values']:
        for val in value['values']:
            fabric_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            fabric_params_list.append({
                 "category_name":"Sarees",
                "filter_type":"fabric",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })


saree_type_list=[]
saree_type_param_list=[]

saree_type=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][5]
if saree_type['title']=="Saree Type":
    for value in saree_type['values']:
        for val in value['values']:
            saree_type_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))

            saree_type_param_list.append({
                 "category_name":"Saree",
                "filter_type":"Saree Type",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })



pattern_list=[]
pattern_param_list=[]
pattern=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][4]
if pattern['title']=="Pattern":
    for value in pattern['values']:
        for val in value['values']:
            pattern_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            pattern_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Pattern",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })


discount_param_list=[]
discount_list=[]
discount=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][3]
if discount['title']=="Discount":
    for value in discount['values']:
        for val in value['values']:
            discount_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            discount_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Discount",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })



gender_param_list=[]
gender_list=[]
gender=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][2]
if gender['title']=="Gender":
    for value in gender['values']:
        for val in value['values']:
            gender_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            gender_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Gender",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })


occasion_param_list=[]
occasion_list=[]
occasion=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][7]
if occasion['title']=="Occasion":
    for value in occasion['values']:
        for val in value['values']:
            occasion_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            occasion_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Occasion",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })


color_param_list=[]
color_list=[]
color=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][8]
if color['title']=="Color":
    for value in color['values']:
        for val in value['values']:
            color_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            color_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Color",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })


saree_style_list=[]
saree_style_param_list=[]
saree_style=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][12]
if saree_style['title']=="Saree Style":
    for value in saree_style['values']:
        for val in value['values']:
            saree_style_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            saree_style_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Saree Style",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })



cutomer_rating_list=[]
cutomer_rating_param_list=[]
cutomer_rating=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][9]
if cutomer_rating['title']=="Customer Ratings":
    for value in cutomer_rating['values']:
        for val in value['values']:
            cutomer_rating_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            cutomer_rating_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Customer Ratings",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"
            })


pack_list=[]
pack_param_list=[]
pack=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][11]
if pack['title']=="Pack of":
    for value in pack['values']:
        for val in value['values']:
            pack_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            pack_param_list.append({
                 "category_name":"Sarees",
                "filter_type":"Pack of",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"


            })

arrival_list=[]
arrival_param_list=[]
arrival=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][13]
if arrival['title']=="New Arrivals":
    for value in arrival['values']:
        for val in value['values']:
            arrival_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            arrival_param_list.append({
                "category_name":"Sarees",
                "filter_type":"New Arrivals",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}"

            })

combined_list=[]
combined_list.extend(brand_params_list)
combined_list.extend(fabric_params_list)
combined_list.extend(saree_type_param_list)
combined_list.extend(pattern_param_list)
combined_list.extend(gender_param_list)
combined_list.extend(occasion_param_list)
combined_list.extend(color_param_list)
combined_list.extend(pack_param_list)
combined_list.extend(arrival_param_list)
combined_list.extend(cutomer_rating_param_list)
combined_list.extend(saree_style_param_list)
combined_list.extend(discount_param_list)

print(len(combined_list))
print(combined_list[0:5])

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',       # change if needed
    user='root',   # change to your MySQL username
    password='Actowiz', # change to your MySQL password
    database='flipkart_saree'  # change to your database name
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS flipkart_filters (
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
        INSERT INTO flipkart_filters (category_name, filter_type, filter_name, slug, url, count, total_count, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        row['category_name'],
        row['filter_type'],
        row['filter_name'],
        row['slug'],
        row['url'],
        0,
        0,
        'pending'
    ))

conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL table successfully.")


