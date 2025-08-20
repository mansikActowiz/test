
from urllib.parse import quote
from parsel import Selector
import mysql.connector
import requests
import json
import time
import random
from curl_cffi import requests

cookies = {
    'Network-Type': '4g',
    'T': 'TI174824499597300142754598348542330031370306090257579454047282066136',
    'vw': '1366',
    'dpr': '1',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'fonts-loaded': 'en_loaded',
    'isH2EnabledBandwidth': 'false',
    'h2NetworkBandwidth': '9',
    'ULSN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwNDEzMDY0MTM0NlhZMVFQQjQiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDA3MzAwMSwiaWF0IjoxNzU0MjkzMDAxLCJqdGkiOiJmNjkxNjlkMS1iZjQ4LTQyYmUtYTZmNy02YTQwMjNkZDJhYTUifQ.SKmnWwLkb78ePUma4KSDEwCPfi3poN8hGsdKbBCJDaU',
    'ud': '1.3RovXtHZlV6Ku4MnxYAGp12z9rswmi-Rm7GUyv5aizXCUI2_V6rn93V7V4ogfQ4fm36i3_Z-aKTDlXSoF8wff_IQZNwjcoc8StHK3heQPEGKiQ7fD2YXEJAqNIjdvPbYIcP0uyVQK_Y7JMx2MsbJpX0PzkH-h809MqE7h0TzhCgNLPAU3b7cXPjoKOGrtttm',
    'Network-Type': '4g',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NTQ2MzA1OTQsImlhdCI6MTc1NDYyODc5NCwiaXNzIjoia2V2bGFyIiwianRpIjoiMmJhMWE3N2EtY2M2Zi00NTI5LTg1NzAtZjM2ZDkwYzFmNGRkIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJYVTVTMlAiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6Ikh1dnp3VVJfMjNfMEVWaEdZVzFudzVlblptUG9DZ2pzaURXcE5iSGpqeFpoZWpBZGNRUm9wZz09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.3xRPgFtgdhDbKqb70F-__GBbhlfvSBO6o7VOJjnZYDA',
    'rt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NzA1MjYzOTQsImlhdCI6MTc1NDYyODc5NCwiaXNzIjoia2V2bGFyIiwianRpIjoiZTQ5MTc3MGQtMTM0Ny00ZTA3LWJlNzYtNTNlMzA1MzM0M2RmIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJYVTVTMlAiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiVDFQWDgxIn0.T0Fh8rmzBBSY0XSlVEsAAs8MMsErxwoalLeW8OHvWBM',
    'vh': '607',
    'K-ACTION': 'null',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20309%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754896184%7C12%7CMCAAMB-1755233571%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754635971s%7CNONE%7CMCAID%7CNONE',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'vd': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872-1754284011313-22.1754629381.1754628794.162519102',
    'S': 'd1t16P2xXclwgW2YvVj9PWiEAU1mll93ngXgLILFCxCqex9cbYFgn9ihjBtZ200SIp99h99PrWnNy4HGhvzRMZKCBMQ==',
    'SN': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK586F478E36664EC6A8895905DD30A39F.1754629390124.LI',
}
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
    # 'Cookie': 'Network-Type=4g; T=TI174824499597300142754598348542330031370306090257579454047282066136; vw=1366; dpr=1; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI1MDgwNDEzMDY0MTM0NlhZMVFQQjQiLCJma0RldiI6bnVsbH0sImV4cCI6MTc3MDA3MzAwMSwiaWF0IjoxNzU0MjkzMDAxLCJqdGkiOiJmNjkxNjlkMS1iZjQ4LTQyYmUtYTZmNy02YTQwMjNkZDJhYTUifQ.SKmnWwLkb78ePUma4KSDEwCPfi3poN8hGsdKbBCJDaU; ud=1.3RovXtHZlV6Ku4MnxYAGp12z9rswmi-Rm7GUyv5aizXCUI2_V6rn93V7V4ogfQ4fm36i3_Z-aKTDlXSoF8wff_IQZNwjcoc8StHK3heQPEGKiQ7fD2YXEJAqNIjdvPbYIcP0uyVQK_Y7JMx2MsbJpX0PzkH-h809MqE7h0TzhCgNLPAU3b7cXPjoKOGrtttm; Network-Type=4g; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NTQ2MzA1OTQsImlhdCI6MTc1NDYyODc5NCwiaXNzIjoia2V2bGFyIiwianRpIjoiMmJhMWE3N2EtY2M2Zi00NTI5LTg1NzAtZjM2ZDkwYzFmNGRkIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJYVTVTMlAiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6Ikh1dnp3VVJfMjNfMEVWaEdZVzFudzVlblptUG9DZ2pzaURXcE5iSGpqeFpoZWpBZGNRUm9wZz09IiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.3xRPgFtgdhDbKqb70F-__GBbhlfvSBO6o7VOJjnZYDA; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3NzA1MjYzOTQsImlhdCI6MTc1NDYyODc5NCwiaXNzIjoia2V2bGFyIiwianRpIjoiZTQ5MTc3MGQtMTM0Ny00ZTA3LWJlNzYtNTNlMzA1MzM0M2RmIiwidHlwZSI6IlJUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJiSWQiOiJYVTVTMlAiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiVDFQWDgxIn0.T0Fh8rmzBBSY0XSlVEsAAs8MMsErxwoalLeW8OHvWBM; vh=607; K-ACTION=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20309%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1754896184%7C12%7CMCAAMB-1755233571%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1754635971s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aid-base-2025-at-store%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; vd=VI5FAAFE7DD4B443C198E5E65ACCA7C872-1754284011313-22.1754629381.1754628794.162519102; S=d1t16P2xXclwgW2YvVj9PWiEAU1mll93ngXgLILFCxCqex9cbYFgn9ihjBtZ200SIp99h99PrWnNy4HGhvzRMZKCBMQ==; SN=VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK586F478E36664EC6A8895905DD30A39F.1754629390124.LI',
}

params = {
    'sid': 'clo,hlg,wrp',
    'otracker': [
        'categorytree',
        'nmenu_sub_Women_0_Lehenga Choli',
    ],
}

base_url='https://www.flipkart.com/clothing-and-accessories/lehenga-choli/women-lehenga-choli/pr?sid=clo,hlg,wrp&otracker=categorytree&otracker=nmenu_sub_Women_0_Lehenga%20Choli'


response = requests.get(base_url,
    params=params,
    cookies=cookies,
    impersonate="chrome110",
    headers=headers,
)
print(response.status_code)



# sleep between 1 to 5 seconds
time.sleep(random.uniform(1, 5))




sel = Selector(text=response.text)

script_data = sel.xpath('//script[contains(text(), "window.__INITIAL_STATE")]/text()').get()

script = script_data.replace('window.__INITIAL_STATE__ = ', '')[:-1]

data=json.loads(script)
# print(data)


brand_params_list = []

id=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][4]

if id["title"] == "Brand":
    for value in id['values']:
        for val in value['values']:
            params_encoded = quote(val.get('resource').get('params'))
            print(params_encoded)
            brand_params_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Brand",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count":val.get('count'),

            })

print( brand_params_list)
print(len(brand_params_list)) #1417
# exit(0)

fabric_params_list=[]
fabric_list=[]
fabric=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][6]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[6].values[0].values[0].title'
if fabric['title'] == "fabric":
    for value in fabric['values']:
        for val in value['values']:
            fabric_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            fabric_params_list.append({
                 "category_name":"Lehenga",
                "filter_type":"fabric",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count":val.get('count'),

            })
# print(fabric_params_list)
print(len(fabric_params_list))  #15

lehenga_type_list=[]
lehenga_type_param_list=[]

lehenga_type=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][5]

if lehenga_type['title']=="Type":
    for value in lehenga_type['values']:
        for val in value['values']:
            lehenga_type_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))

            lehenga_type_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Lehenga Type",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

# print(lehenga_type_param_list)
print(len(lehenga_type_param_list))

pattern_list=[]
pattern_param_list=[]
pattern=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][8]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[8].values[0].values[0].title'
if pattern['title']=="Pattern":
    for value in pattern['values']:
        for val in value['values']:
            pattern_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            pattern_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Pattern",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })


print(len(pattern_param_list))

discount_param_list=[]
discount_list=[]
discount=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][12]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[12].values[0].values[0].title'
if discount['title']=="Discount":
    for value in discount['values']:
        for val in value['values']:
            discount_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            discount_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Discount",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

# print(discount_param_list)
print(len(discount_param_list))

gender_param_list=[]
gender_list=[]
gender=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][14]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[14].values[0].values[0].title'
if gender['title']=="Gender":
    for value in gender['values']:
        for val in value['values']:
            gender_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            gender_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Gender",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
# print(gender_param_list)
print(len(gender_param_list))


occasion_param_list=[]
occasion_list=[]
occasion=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][7]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[7].values[0].values[0].title'
if occasion['title']=="Occasion":
    for value in occasion['values']:
        for val in value['values']:
            occasion_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            occasion_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Occasion",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
# print(occasion_param_list)
print(len(occasion_param_list))

color_param_list=[]
color_list=[]
color=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][10]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[10].values[0].values[0].title'
if color['title']=="Color":
    for value in color['values']:
        for val in value['values']:
            color_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            color_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Color",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })


collection_list=[]
collection_param_list=[]
collection=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][16]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[16].values[0].values[0].title'
if collection['title']=="Collections":
    for value in collection['values']:
        for val in value['values']:
            collection_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            collection_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Collection",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })
# print(collection_param_list)
print(len(collection_param_list))


cutomer_rating_list=[]
cutomer_rating_param_list=[]
cutomer_rating=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][2]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[2].values[0].values[0].title'
if cutomer_rating['title']=="Customer Ratings":
    for value in cutomer_rating['values']:
        for val in value['values']:
            cutomer_rating_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            cutomer_rating_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Customer Ratings",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),
            })
# print(cutomer_rating_param_list)
print(len(cutomer_rating_param_list))



sleeve_list=[]
sleeve_param_list=[]
sleeve=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][13]
# 'pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[13].values[0].values[0].title'
if sleeve['title']=="Sleeve":
    for value in sleeve['values']:
        for val in value['values']:
            sleeve_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            sleeve_param_list.append({
                 "category_name":"Lehenga",
                "filter_type":"Sleeve",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),


            })
# print(sleeve_param_list)
print(len(sleeve_param_list))


arrival_list=[]
arrival_param_list=[]
arrival=data['pageDataV4']['page']['data']['10002'][0]['widget']['data']['filters']['facetResponse']['facets'][15]
# pageDataV4.page.data[10002][0].widget.data.filters.facetResponse.facets[15].values[0].values[0].title
if arrival['title']=="New Arrivals":
    for value in arrival['values']:
        for val in value['values']:
            arrival_list.append(val['title'])
            params_encoded = quote(val.get('resource').get('params'))
            arrival_param_list.append({
                "category_name":"Lehenga",
                "filter_type":"New Arrivals",
                "filter_name":val.get('title'),
                "slug":val.get('resource').get('params'),
                "url":f"{base_url}&p%5B%5D={params_encoded}",
                "count": val.get('count'),

            })

# print(arrival_param_list)
print(len(arrival_param_list))
# exit(0)

combined_list=[]
combined_list.extend(brand_params_list)
combined_list.extend(fabric_params_list)
combined_list.extend(lehenga_type_param_list)
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

# exit(0)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',       # change if needed
    user='root',   # change to your MySQL username
    password='Actowiz', # change to your MySQL password
    database='flipkart_lehenga'  # change to your database name
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS flipkart_lehenga_filters (
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
        INSERT INTO flipkart_lehenga_filters (category_name, filter_type, filter_name, slug, url, count, total_count, status)
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


