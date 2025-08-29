from curl_cffi import requests
import requests
import random
import gzip
from parsel import Selector
import json
import csv
import re
import pandas as pd

cookies = {
    '99_ab': '29',
    'GOOGLE_SEARCH_ID': '5996471749034946122',
    'xAB': 'SuperControlGroup%3D61%3AN%2CRECOMLANDINGPAGE%3D19%3AY%2CtopMatchHandlingAB%3D98%3AD%2CxidHandlingAB%3D19%3AY%2CseamlessLogin%3D36%3AY',
    'hp_bcf_data': '',
    '__utmc': '267917265',
    '_gcl_au': '1.1.942156623.1749034924',
    '_gid': 'GA1.2.893255392.1749034924',
    '_hjSession_3171461': 'eyJpZCI6ImFhY2JhNjg2LWYyM2MtNDhkNC04NTc4LTNkZmFhMWI0NGEwYiIsImMiOjE3NDkwMzQ5MjQzNDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_fbp': 'fb.1.1749034925195.640816846548180865',
    '_clck': '14r7k68%7C2%7Cfwh%7C0%7C1981',
    'session_source': 'https://www.google.com/',
    'landmark_toast': 'true',
    'showCookieBanner': '1',
    '_gcl_gs': '2.1.k1$i1749034956$u185700833',
    '_gac_UA-224016-1': '1.1749034961.CjwKCAjw3f_BBhAPEiwAaA3K5FOWXlCOEkDP5lGIDEszCb9-jzzj_Gqss31-UzkfUl8qIg8nxKBSEBoCKXIQAvD_BwE',
    '_hjSessionUser_3171461': 'eyJpZCI6IjM3MGIyYmI1LWEyNGQtNTAxOS1iNDFlLWJhODA2OTA2Zjc1YyIsImNyZWF0ZWQiOjE3NDkwMzQ5MjQzNDAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gcl_aw': 'GCL.1749034979.CjwKCAjw3f_BBhAPEiwAaA3K5FOWXlCOEkDP5lGIDEszCb9-jzzj_Gqss31-UzkfUl8qIg8nxKBSEBoCKXIQAvD_BwE',
    '__utma': '267917265.420285098.1749034922.1749034961.1749035129.3',
    '__utmz': '267917265.1749035129.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmt': '1',
    '__utmb': '267917265.7.10.1749035129',
    '_ga_9QHC0XEKPS': 'GS2.1.s1749034924$o1$g1$t1749036601$j34$l0$h0',
    '_ga': 'GA1.2.1257563700.1749034924',
    '_uetsid': '5929d3c0413311f0b6200b447584fb53',
    '_uetvid': '592a0210413311f0be885b99c5e3a6db',
    '_clsk': '131ufik%7C1749036602331%7C4%7C0%7Cl.clarity.ms%2Fcollect',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://www.99acres.com/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    # 'cookie': '99_ab=29; GOOGLE_SEARCH_ID=5996471749034946122; xAB=SuperControlGroup%3D61%3AN%2CRECOMLANDINGPAGE%3D19%3AY%2CtopMatchHandlingAB%3D98%3AD%2CxidHandlingAB%3D19%3AY%2CseamlessLogin%3D36%3AY; hp_bcf_data=; __utmc=267917265; _gcl_au=1.1.942156623.1749034924; _gid=GA1.2.893255392.1749034924; _hjSession_3171461=eyJpZCI6ImFhY2JhNjg2LWYyM2MtNDhkNC04NTc4LTNkZmFhMWI0NGEwYiIsImMiOjE3NDkwMzQ5MjQzNDEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1749034925195.640816846548180865; _clck=14r7k68%7C2%7Cfwh%7C0%7C1981; session_source=https://www.google.com/; landmark_toast=true; showCookieBanner=1; _gcl_gs=2.1.k1$i1749034956$u185700833; _gac_UA-224016-1=1.1749034961.CjwKCAjw3f_BBhAPEiwAaA3K5FOWXlCOEkDP5lGIDEszCb9-jzzj_Gqss31-UzkfUl8qIg8nxKBSEBoCKXIQAvD_BwE; _hjSessionUser_3171461=eyJpZCI6IjM3MGIyYmI1LWEyNGQtNTAxOS1iNDFlLWJhODA2OTA2Zjc1YyIsImNyZWF0ZWQiOjE3NDkwMzQ5MjQzNDAsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_aw=GCL.1749034979.CjwKCAjw3f_BBhAPEiwAaA3K5FOWXlCOEkDP5lGIDEszCb9-jzzj_Gqss31-UzkfUl8qIg8nxKBSEBoCKXIQAvD_BwE; __utma=267917265.420285098.1749034922.1749034961.1749035129.3; __utmz=267917265.1749035129.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=267917265.7.10.1749035129; _ga_9QHC0XEKPS=GS2.1.s1749034924$o1$g1$t1749036601$j34$l0$h0; _ga=GA1.2.1257563700.1749034924; _uetsid=5929d3c0413311f0b6200b447584fb53; _uetvid=592a0210413311f0be885b99c5e3a6db; _clsk=131ufik%7C1749036602331%7C4%7C0%7Cl.clarity.ms%2Fcollect',
}

params = {
    'city': '45',
    'res_com': 'R',
    'preference': 'S',
    'price_min': '0',
    'price_max': '0',
    'availability': '',
    'bedroom_num': '',
    'locality_array': '',
    'class': '',
    'property_type': '',
    'transact_type': '',
    'building_id': '',
    'tenant_pref': '',
    'sharing': '',
}

# while True:

response = requests.get('https://www.99acres.com/search/property/buy',
                        params=params,
                        # cookies=cookies,
                        headers=headers,
                        impersonate="chrome101",
                        )
    # if "Ahmedabad" in response.text:
    #     print("Yes")
    # else:
    #     print("No")


raw_html=response.text
print(response.text)
print(response.status_code)
output_path = r'C:\Users\Madri.Gadani\Desktop\madri\99acres\99acres_html.html'
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')