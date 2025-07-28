



import requests
from urllib.parse import quote

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'origin': 'https://www.croma.com',
    'priority': 'u=1, i',
    'referer': 'https://www.croma.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

# Dynamic input
keyword = "mobile"
brand = "Vivo"
color = "BLACK"
price_min = "10,001"
price_max = "20,000"
aa='256GB'

# URL-encoded price range
price_range = quote(f"{price_min} - {price_max}")

# Final request
url = f'https://api.croma.com/searchservices/v1/search?currentPage=0&query={keyword}:relevance:SG-ManufacturerDetails-Brand:{brand}:price_group:{price_range}:SG-M%26TStorageSpecifications-InternalStorage:{aa}:SG-ProductAesthetics-ColorFamily:{color}&fields=FULL&channel=WEB&channelCode=400049&spellOpt=DEFAULT'

response = requests.get(url, headers=headers)
print(response.status_code)
# new_url='https://api.croma.com/searchservices/v1/search?currentPage=0&query=mobile%3Arelevance%3ASG-ManufacturerDetails-Brand%3AVivo%3ASG-M%2526TStorageSpecifications-InternalStorage%3A256GB%3ASG-ProductAesthetics-ColorFamily%3ABLACK%3Aprice_group%3A10%252C001%2520-%252020%252C000&fields=FULL&channel=WEB&spellOpt=DEFAULT'
# response1 = requests.get(new_url, headers=headers)
# print(response1.status_code)

# Output
print("Status code:", response.status_code)
with open("abc.html", "w", encoding="utf-8") as f:
    f.write(response.text)












