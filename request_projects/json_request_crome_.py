import json
def search_key(search):
    import requests
    import json

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

    params = {
        'currentPage': '0',
        'query': f'{search}:relevance',
        'fields': 'FULL',
        'channel': 'WEB',
        'spellOpt': 'DEFAULT',
    }

    response = requests.get('https://api.croma.com/searchservices/v1/search', params=params, headers=headers)
    print(response.status_code)
    raw_html=response.text
    print(raw_html)
    print('//////////////////////////////////////')
    data = json.loads(response.text)
    print(data)
    print('.............................................')

    data_json = json.dumps(data, indent=4)
    print(data_json)

    details=data['products']

    product_list=[]

    croma_url='https://www.croma.com'

    for product in details:
        product_url=croma_url+product['url']
        productID=product['code']
        productName=product['name']
        productImage=product['plpImage']
        listingPrice=product['mrp']['formattedValue'].replace('₹','')
        sellingPrice=product['price']['formattedValue'].replace('₹','')
        review=product['numberOfRatings']
        rating=round(product['averageRating'],2)
        discount=product['discountValue']
        description_html=product['quickViewDesc']

        if description_html.startswith("<ul>") and description_html.endswith("</ul>"):
            description_html = description_html[4:-5]

            # Remove <li> and split by </li>
        description_items = []
        for item in description_html.split('</li>'):
            item = item.replace('<li>', '').strip()
            if item:
                description_items.append(item)

        product_dict={
            'productURL':product_url,
            'productID':productID,
            'productName':productName,
            'productImage':productImage,
            'listingPrice':listingPrice,
            'sellingPrice':sellingPrice,
            'discount': discount,
            'features': description_items,
            'review':review,
            'rating':rating

            }

        product_list.append(product_dict)

    return product_list
data = search_key("iphone")
print(json.dumps(data))


def write_to_json(all_stored_data_lst,json_output_path):
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump( all_stored_data_lst, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to JSON path: {json_output_path}")

json_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\croma_search\croma_iphone_search_json1.json'
# write_to_json(data,json_output_path)

