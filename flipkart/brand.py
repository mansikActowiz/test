import requests
from parsel import Selector
import random
import gzip
from parsel import Selector
import time
import csv
import requests
import requests


cookies = {
    'Network-Type': '4g',
    'T': 'TI174824499597300142754598348542330031370306090257579454047282066136',
    'rt': 'null',
    'K-ACTION': 'null',
    'ud': '7._EA8MPay8RgQCnXpsBXZHDhEvrPi_FigMKvNKmSmvPkYNsXpjGM3sYBdoc3UdkrlNyE0WjSJs9YHBeCXrvRRnRlm3F8DwKy2yKyTzWwt15btu3Dh9NCHLAZB5HSBDMKK9HnDy5_h6L6yK5COVaD2Aw',
    'vw': '1366',
    'dpr': '1',
    'vh': '641',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3NTU0MTI4ODAsImlhdCI6MTc1MzY4NDg4MCwiaXNzIjoia2V2bGFyIiwianRpIjoiMTBmODRlN2MtYjYwZC00NTQxLTgzYjAtNGQ4MTc2YWQyODYzIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.uRkVBGj_YPFHtMKQyqsrWf5wigFoikhZTAV7iCMaCvs',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'Network-Type': '4g',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20302%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754289652%7C12%7CMCAAMB-1754622877%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754025277s%7CNONE%7CMCAID%7CNONE',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'vd': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872-1748244997568-25.1754020985.1754017754.163439705',
    'S': 'd1t16Pz9MTj99Pz9PPz8fST8EP+ZO54wrqFnBw3mVTQCDooFGHj1V8d2pOFcOKwttS5AMtjbVJn26GLESZCo9m7jLjA==',
    'SN': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOKDB4F35E4133A4C6084AACB725B67E80F.1754020985965.LO',
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
response = requests.get(url_brand,
    cookies=cookies,
    headers=headers,
)


import json
response_brand = requests.get(url_brand, headers=headers)
sel = Selector(text=response_brand.text)
# print(sel)

script_data = sel.xpath('//script[contains(text(), "window.__INITIAL_STATE")]/text()').get()



script = script_data.replace('window.__INITIAL_STATE__ = ', '')[:-1]


data=json.loads(script)


brand_list = list()

params_list = []
title=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][1]['values'][0]['values'][0]['title']
id=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][1]
''
if id["title"] == "Brand":
    for value in id['values']:
        for val in value['values']:
            params_list.append(val.get('resource').get('params'))
            brand_list.append(val['title'])

print(params_list)

fabric_params_list=[]
fabric_list=[]
fabric=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][6]

if fabric['title'] == "fabric":
    for value in fabric['values']:
        for val in value['values']:
            fabric_list.append(val['title'])
            fabric_params_list.append(val.get('resource').get('params'))
print(len(fabric_list))
print(fabric_list)
print(fabric_params_list)

saree_type_list=[]
saree_type_param_list=[]

saree_type=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][5]
if saree_type['title']=="Saree Type":
    for value in saree_type['values']:
        for val in value['values']:
            saree_type_list.append(val['title'])
            saree_type_param_list.append(val.get('resource').get('params'))

print(len(saree_type_list))
# print(saree_type_list)
print(saree_type_param_list)

pattern_list=[]
pattern_param_list=[]
pattern=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][4]
if pattern['title']=="Pattern":
    for value in pattern['values']:
        for val in value['values']:
            pattern_list.append(val['title'])
            pattern_param_list.append(val.get('resource').get('params'))

print(len(pattern_list))
print(pattern_param_list)

discount_param_list=[]
discount_list=[]
discount=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][3]
if discount['title']=="Discount":
    for value in discount['values']:
        for val in value['values']:
            discount_list.append(val['title'])
            discount_param_list.append(val.get('resource').get('params'))

print(len(discount_list))
print(discount_param_list)



gender_param_list=[]
gender_list=[]
gender=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][2]
if gender['title']=="Gender":
    for value in gender['values']:
        for val in value['values']:
            gender_list.append(val['title'])
            gender_param_list.append(val.get('resource').get('params'))

print(len(gender_list))
print(gender_param_list)

occasion_param_list=[]
occasion_list=[]
occasion=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][7]
if occasion['title']=="Occasion":
    for value in occasion['values']:
        for val in value['values']:
            occasion_list.append(val['title'])
            occasion_param_list.append(val.get('resource').get('params'))

print(len(occasion_list))
print(occasion_param_list)


color_param_list=[]
color_list=[]
color=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][8]
if color['title']=="Color":
    for value in color['values']:
        for val in value['values']:
            color_list.append(val['title'])
            color_param_list.append(val.get('resource').get('params'))

print(len(color_list))
print(color_param_list)

saree_style_list=[]
saree_style_param_list=[]
saree_style=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][12]
if saree_style['title']=="Saree Style":
    for value in saree_style['values']:
        for val in value['values']:
            saree_style_list.append(val['title'])
            saree_style_param_list.append(val.get('resource').get('params'))

print(len(saree_style_list))
print(saree_style_param_list)



cutomer_rating_list=[]
cutomer_rating_param_list=[]
cutomer_rating=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][9]
if cutomer_rating['title']=="Customer Ratings":
    for value in cutomer_rating['values']:
        for val in value['values']:
            cutomer_rating_list.append(val['title'])
            cutomer_rating_param_list.append(val.get('resource').get('params'))

print(len(cutomer_rating_list))
print(cutomer_rating_param_list)


pack_list=[]
pack_param_list=[]
pack=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][11]
if pack['title']=="Pack of":
    for value in pack['values']:
        for val in value['values']:
            pack_list.append(val['title'])
            pack_param_list.append(val.get('resource').get('params'))
            # 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[17].title'

print(len(pack_list))
print(pack_param_list)


arrival_list=[]
arrival_param_list=[]
arrival=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][13]
if arrival['title']=="New Arrivals":
    for value in arrival['values']:
        for val in value['values']:
            arrival_list.append(val['title'])
            arrival_param_list.append(val.get('resource').get('params'))

print(len(arrival_list))
print(arrival_param_list)



