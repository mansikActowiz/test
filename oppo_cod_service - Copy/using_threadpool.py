import pandas as pd
from curl_cffi import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


# df=pd.read_csv(r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\oppo_cod_service\zipcode.csv', encoding='latin1')
# print(df)


df = pd.read_csv(r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\oppo_cod_service\zipcode_new.csv', encoding='latin1')
zip_list = df.iloc[:, 0].tolist()
print(f"Total pincodes: {len(zip_list)}")
# exit(0)
product_url = 'https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169'
results = []

cookies = {
    'frontend': 'f96ca3fb3c014cb887b870a98c793262',
    '_gcl_au': '1.1.1940824571.1755234576',
    '_ga': 'GA1.1.1842047036.1755234576',
    'WEBSITE_URL': product_url,
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.oppo.com',
    'referer': 'https://www.oppo.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

save_path = r"D:\madri_new_codes\oppo\saved_json_all_pincodes_threads"
os.makedirs(save_path, exist_ok=True)


def process_pincode(i):
    json_data = {
        'productType': 1,
        'pinCode': f'{i}',
        'skuItems': [
            {'skuCode': '5011100260'},
            {'skuCode': '5011100261'},
            {'skuCode': '5011100262'},
            {'skuCode': '5011100263'},
            {'skuCode': '5011100264'},
            {'skuCode': '5011100265'},
        ],
        'storeViewCode': 'in',
        'storeCode': 'in',
        'configModule': 3,
        'countryCode': 'IN',
        'deviceType': 2,
        'source': 1,
    }

    response = requests.post(
        'https://opsg-gateway-in.oppo.com/v2/api/rest/mall/inventory/estimate/time/fetch',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(f'Response of zipcode {i}:', response.status_code)

    data = json.loads(response.text)

    with open(os.path.join(save_path, f'pincode_{i}.json'), 'w', encoding='utf-8') as f:
        f.write(response.text)

    service_availability = 0 if data.get('data') is None else 1

    cod_availability = 0  # default
    if data.get('data') and data['data'].get('skuDetailShippingInfoMap'):
        sku_map = data['data']['skuDetailShippingInfoMap']
        if "5011100260" in sku_map and sku_map["5011100260"]:
            if sku_map["5011100260"][0].get('shippingMethodCode') == "BlueDart-COD":
                cod_availability = 1

    return {
        'pincode': i,
        'Product_url': product_url,
        'service_availability': service_availability,
        'cod_availability': cod_availability
    }


# --- ThreadPool Execution (instead of simple for loop) ---
results = []
with ThreadPoolExecutor(max_workers=3) as executor:  # adjust workers as needed
    future_to_pin = {executor.submit(process_pincode, i): i for i in zip_list}

    for future in as_completed(future_to_pin):
        try:
            results.append(future.result())
        except Exception as e:
            print(f"Error for {future_to_pin[future]}: {e}")

output_df = pd.DataFrame(results)
print(output_df)

oppo_output_csv = r'D:\madri_new_codes\oppo\oppo_output_csv\oppo_scope_2_all_pincodes_threads_new.csv'
os.makedirs(os.path.dirname(oppo_output_csv), exist_ok=True)
output_df.to_csv(oppo_output_csv, index=False)
