import requests
from urllib.parse import quote
import time
import json

# Headers
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'origin': 'https://www.croma.com',
    'referer': 'https://www.croma.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
}

# Filters
keyword = "mobile"
brand = "Samsung"
color = "BLACK"
price_min = "10,001"
price_max = "20,000"
storage = '128GB'
croma_url = "https://www.croma.com"

# Encode price range
price_range = quote(f"{price_min} - {price_max}")


def query_build():
# Build query
    query_parts = [
        f"{keyword}",
        "relevance",
        f"SG-ManufacturerDetails-Brand:{brand}",
        f"price_group:{price_range}",
        f"SG-ProductAesthetics-ColorFamily:{color}"
    ]

    if keyword.lower() == "mobile":
        query_parts.append(f"SG-M%26TStorageSpecifications-InternalStorage:{storage}")

    query = ":".join(query_parts)
    print(query)
    return query
my_query=query_build()
base_url = f"https://api.croma.com/searchservices/v1/search?query={my_query}&fields=FULL&channel=WEB&channelCode=400049&spellOpt=DEFAULT"
print(base_url)

def search_key():



# Initialize
    current_page = 0
    product_list = []

    # Loop through all pages
    while True:
        url = f"{base_url}&currentPage={current_page}"
        response = requests.get(url, headers=headers)
        print(f"🔗 Request URL: {response.url}")

        if response.status_code != 200:
            print(f"❌ Failed to fetch page {current_page}, status code: {response.status_code}")
            break

        data = response.json()

        if 'products' in data and data['products']:
            products = data['products']
            print(f"📄 Processing page {current_page} with {len(products)} products")

            for product in products:
                try:
                    productURL = croma_url + product['url']
                    productID = product['code']
                    productName = product['name']
                    productImage = product['plpImage']
                    listingPrice = product.get('mrp', {}).get('formattedValue', '').replace('₹', '').replace(',', '').strip()
                    sellingPrice = product.get('price', {}).get('formattedValue', '').replace('₹', '').replace(',', '').strip()
                    discount = product.get('discountValue', '').replace('%', '').strip()
                    features = [
                        item.replace('<li>', '').strip()
                        for item in product.get('quickViewDesc', '')[4:-5].split('</li>')
                        if item
                    ] if product.get('quickViewDesc', '').startswith('<ul>') else []
                    review = product.get('numberOfRatings', 0)
                    rating = round(product.get('averageRating', 0.0), 2)

                    product_dict = {
                        'productURL': productURL,
                        'productID': productID,
                        'productName': productName,
                        'productImage': productImage,
                        'listingPrice': listingPrice,
                        'sellingPrice': sellingPrice,
                        'discount': discount,
                        'features': features,
                        'review': review,
                        'rating': rating
                    }

                    product_list.append(product_dict)

                except Exception as e:
                    print(f"⚠️ Error processing product: {e}")

            # ✅ Advance to the next page
            current_page += 1
            time.sleep(0.5)

        else:
            # ❌ No more products/pages
            print("🚫 No more products found.")
            break

# Output total products
print(f"\n✅ Total products fetched: {len(product_list)}")
