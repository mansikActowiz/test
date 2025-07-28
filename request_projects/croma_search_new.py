import gzip
import json
from curl_cffi import requests

# Base and search URLs
base_url = 'https://www.croma.com/'
search_url = base_url + 'searchB?q=ac%3Arelevance&text=ac'

# Headers and cookies
headers = {
    'accept': 'application/json, text/html;q=0.9,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

# Output paths
html_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_search\croma_homepage.html'
html_gz_path = html_path + '.gz'
product_json_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_search\croma_ac_products.json'
product_txt_path = r'C:\Users\Madri.Gadani\Desktop\madri\croma_search\croma_ac_products.txt'

# Step 1: Get homepage HTML
response = requests.get(base_url, headers=headers, impersonate="chrome120")
print(f"Homepage status code: {response.status_code}")

# Save HTML and compress
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(response.text)
print("Homepage HTML saved.")

with open(html_path, 'rb') as file_in, gzip.open(html_gz_path, 'wb') as file_out:
    file_out.writelines(file_in)
print("Compressed HTML saved.")

# Step 2: Fetch product data
response_product = requests.get(search_url, headers=headers, impersonate="chrome120")
print(f"Product search status code: {response_product.status_code}")

# Step 3: Parse product data (if JSON response is valid)
try:
    data = response_product.json()
    products = data.get('products', data.get('productsView', {}).get('products', []))  # handles different key paths
    print(f"Found {len(products)} products.")

    # Save raw JSON
    with open(product_json_path, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=2)
    print("Product data saved as JSON.")

    # Save readable product info
    with open(product_txt_path, 'w', encoding='utf-8') as f:
        for i, prod in enumerate(products, 1):
            title = prod.get('name') or prod.get('title') or 'N/A'
            price = prod.get('price', {}).get('finalPrice') or prod.get('price') or 'N/A'
            f.write(f"{i}. {title} - ₹{price}\n")
    print("Product info saved as text.")

except Exception as e:
    print("Failed to parse JSON or extract products:", str(e))
