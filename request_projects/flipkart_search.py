

import requests
from parsel import Selector

cookies = {
    'T': 'TI174824499597300142754598348542330031370306090257579454047282066136',
    'rt': 'null',
    'K-ACTION': 'null',
    'ud': '7._EA8MPay8RgQCnXpsBXZHDhEvrPi_FigMKvNKmSmvPkYNsXpjGM3sYBdoc3UdkrlNyE0WjSJs9YHBeCXrvRRnRlm3F8DwKy2yKyTzWwt15btu3Dh9NCHLAZB5HSBDMKK9HnDy5_h6L6yK5COVaD2Aw',
    'vh': '641',
    'vw': '1366',
    'dpr': '1',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NTEyNTc3NTYsImlhdCI6MTc0OTUyOTc1NiwiaXNzIjoia2V2bGFyIiwianRpIjoiNmNmMWJiZmItNmZhMi00NmQzLTg4NGQtMWQ2ZDQ0OGZlMzI1IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.kkRip_Ib9B7PQ_BN_Q8i9qGQokimsqFPZeYnHZXl-HE',
    'fonts-loaded': 'en_loaded',
    'Network-Type': '4g',
    'isH2EnabledBandwidth': 'true',
    'h2NetworkBandwidth': '9',
    'qH': 'df53ca268240ca76',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20250%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1749532110%7C12%7CMCAAMB-1750134539%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1749536939s%7CNONE%7CMCAID%7CNONE',
    'S': 'd1t16XV90eD8/WGQ/Pz8/Pz8/P0VAcUgOr3D20yRkAd7p2c+h1Fat+vagpz2UN6TKXajCVcR29IygF00VZJ1O89uirA==',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'SN': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK82EBFC33C3264387AEC2AE4DC39702E6.1749529821486.LO',
    'vd': 'VI5FAAFE7DD4B443C198E5E65ACCA7C872-1748244997568-11.1749529821.1749529756.163545204',
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version': '"137.0.7151.69"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.69", "Chromium";v="137.0.7151.69", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    # 'Cookie': 'T=TI174824499597300142754598348542330031370306090257579454047282066136; rt=null; K-ACTION=null; ud=7._EA8MPay8RgQCnXpsBXZHDhEvrPi_FigMKvNKmSmvPkYNsXpjGM3sYBdoc3UdkrlNyE0WjSJs9YHBeCXrvRRnRlm3F8DwKy2yKyTzWwt15btu3Dh9NCHLAZB5HSBDMKK9HnDy5_h6L6yK5COVaD2Aw; vh=641; vw=1366; dpr=1; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3NTEyNTc3NTYsImlhdCI6MTc0OTUyOTc1NiwiaXNzIjoia2V2bGFyIiwianRpIjoiNmNmMWJiZmItNmZhMi00NmQzLTg4NGQtMWQ2ZDQ0OGZlMzI1IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzQ4MjQ0OTk1OTczMDAxNDI3NTQ1OTgzNDg1NDIzMzAwMzEzNzAzMDYwOTAyNTc1Nzk0NTQwNDcyODIwNjYxMzYiLCJrZXZJZCI6IlZJNUZBQUZFN0RENEI0NDNDMTk4RTVFNjVBQ0NBN0M4NzIiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.kkRip_Ib9B7PQ_BN_Q8i9qGQokimsqFPZeYnHZXl-HE; fonts-loaded=en_loaded; Network-Type=4g; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; qH=df53ca268240ca76; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20250%7CMCMID%7C40871597148130244842658583104699043135%7CMCAAMLH-1749532110%7C12%7CMCAAMB-1750134539%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1749536939s%7CNONE%7CMCAID%7CNONE; S=d1t16XV90eD8/WGQ/Pz8/Pz8/P0VAcUgOr3D20yRkAd7p2c+h1Fat+vagpz2UN6TKXajCVcR29IygF00VZJ1O89uirA==; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; SN=VI5FAAFE7DD4B443C198E5E65ACCA7C872.TOK82EBFC33C3264387AEC2AE4DC39702E6.1749529821486.LO; vd=VI5FAAFE7DD4B443C198E5E65ACCA7C872-1748244997568-11.1749529821.1749529756.163545204',
}

params = {
    'q': 'refrigerator',
    'otracker': 'search',
    'otracker1': 'search',
    'marketplace': 'FLIPKART',
    'as-show': 'on',
    'as': 'off',
    'as-pos': '1',
    'as-type': 'HISTORY',
}

response = requests.get('https://www.flipkart.com/search', params=params, cookies=cookies, headers=headers)
print(response.status_code)



raw_html=response.text
# print(raw_html)

selector=Selector(text=raw_html)
print(selector)


product=selector.xpath('//div[@class="tUxRFH"]')
print(len(product))

name=selector.xpath('//div[@class="tUxRFH"]//div[@class="KzDlHZ"]/text()').getall()
print(name)



# for i in product:
#     name=

# product = selector.xpath('//div[contains(@class,"slAVV4")]')
# print(f"Found {len(product)} products on this page")
#
# p=selector.xpath('//div[@class="slAVV4"]')
# print(f"Found {len(p)} products on this page")