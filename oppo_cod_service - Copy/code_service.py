# import requests
import pandas as pd
from curl_cffi import requests
import json


cookies = {
    '_gcl_au': '1.1.460456989.1755231191',
    '_ga': 'GA1.1.290520997.1755231191',
    '_fbp': 'fb.1.1755231191530.149646174398811852',
    '_clck': 'yhxw1r%7C2%7Cfyh%7C0%7C2053',
    '_hjSessionUser_2052333': 'eyJpZCI6IjVlY2U5YWMxLWIwYWQtNTJmZi1iZmFjLTYzOTcwZDE5Zjk4NCIsImNyZWF0ZWQiOjE3NTUyMzExOTEzODcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_clsk': 'rhmt3w%7C1755231198241%7C2%7C1%7Cb.clarity.ms%2Fcollect',
    'frontend': '4c043e69b0f544689e0424d2b4b36c4e',
    'IR_gbd': 'oppo.com',
    '_hjSession_2075538': 'eyJpZCI6ImY2YWVmYWRjLThlOWQtNGY0MS1hNzcyLWQ4M2U2NjllMDkwNyIsImMiOjE3NTUyMzEyMTc2MzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    'WEBSITE_URL': 'https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169',
    '_hjSessionUser_2075538': 'eyJpZCI6ImQ1NzUwODQ4LWM5M2MtNWRhZS1hMGY2LWY1Y2ZlMGQ3ODIzZCIsImNyZWF0ZWQiOjE3NTUyMzEyMTc2MzcsImV4aXN0aW5nIjp0cnVlfQ==',
    'IR_15008': '1755232915003%7C0%7C1755232915003%7C%7C',
    '_ga_DTXFPC1MML': 'GS2.1.s1755231191$o1$g1$t1755233048$j45$l0$h0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    'graytag': 'gray',
    'origin': 'https://www.oppo.com',
    'priority': 'u=1, i',
    'referer': 'https://www.oppo.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.460456989.1755231191; _ga=GA1.1.290520997.1755231191; _fbp=fb.1.1755231191530.149646174398811852; _clck=yhxw1r%7C2%7Cfyh%7C0%7C2053; _hjSessionUser_2052333=eyJpZCI6IjVlY2U5YWMxLWIwYWQtNTJmZi1iZmFjLTYzOTcwZDE5Zjk4NCIsImNyZWF0ZWQiOjE3NTUyMzExOTEzODcsImV4aXN0aW5nIjp0cnVlfQ==; _clsk=rhmt3w%7C1755231198241%7C2%7C1%7Cb.clarity.ms%2Fcollect; frontend=4c043e69b0f544689e0424d2b4b36c4e; IR_gbd=oppo.com; _hjSession_2075538=eyJpZCI6ImY2YWVmYWRjLThlOWQtNGY0MS1hNzcyLWQ4M2U2NjllMDkwNyIsImMiOjE3NTUyMzEyMTc2MzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; WEBSITE_URL=https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169; _hjSessionUser_2075538=eyJpZCI6ImQ1NzUwODQ4LWM5M2MtNWRhZS1hMGY2LWY1Y2ZlMGQ3ODIzZCIsImNyZWF0ZWQiOjE3NTUyMzEyMTc2MzcsImV4aXN0aW5nIjp0cnVlfQ==; IR_15008=1755232915003%7C0%7C1755232915003%7C%7C; _ga_DTXFPC1MML=GS2.1.s1755231191$o1$g1$t1755233048$j45$l0$h0',
}

json_data = {
    'productCode': 'P1100169',
    'userGroupName': '',
    'storeViewCode': 'in',
    'storeCode': 'in',
    'configModule': 3,
    'countryCode': 'IN',
    'deviceType': 2,
    'source': 1,
}

response = requests.post(
    'https://opsg-gateway-in.oppo.com/v2/api/rest/mall/product/page/detail/fetch',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.status_code)


df=pd.read_csv(r'C:\Users\Madri.Gadani\PycharmProjects\PythonProject\oppo_cod_service\zipcode.csv', encoding='latin1')
print(df)
exit(0)
zip_list=df.iloc[:, 0].tolist()
print(zip_list)
print(len(zip_list))
product_url='https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169'
results = []
# zip_list=['560085']

cookies = {
    'frontend': 'f96ca3fb3c014cb887b870a98c793262',
    '_gcl_au': '1.1.1940824571.1755234576',
    '_ga': 'GA1.1.1842047036.1755234576',
    'WEBSITE_URL': 'https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169',
    '_hjSession_2075538': 'eyJpZCI6ImRkNzgxMzkzLThhM2EtNDVmYi1hNzllLTViM2IyNjI1NTEwMiIsImMiOjE3NTUyMzQ1NzY5NDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    'IR_gbd': 'oppo.com',
    '_fbp': 'fb.1.1755234576955.414896513993728546',
    '_ga_DTXFPC1MML': 'GS2.1.s1755234576$o1$g1$t1755234581$j55$l0$h0',
    'IR_15008': '1755234582200%7C0%7C1755234582200%7C%7C',
    '_hjSessionUser_2075538': 'eyJpZCI6IjU5ODJiODI0LTAxOWYtNTA1ZC05ODRlLTllMWI4Y2YxMzZhMiIsImNyZWF0ZWQiOjE3NTUyMzQ1NzY5NDUsImV4aXN0aW5nIjp0cnVlfQ==',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    'graytag': 'gray',
    'origin': 'https://www.oppo.com',
    'priority': 'u=1, i',
    'referer': 'https://www.oppo.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'frontend=f96ca3fb3c014cb887b870a98c793262; _gcl_au=1.1.1940824571.1755234576; _ga=GA1.1.1842047036.1755234576; WEBSITE_URL=https://www.oppo.com/in/product/oppo-a3x-5g.P.P1100169; _hjSession_2075538=eyJpZCI6ImRkNzgxMzkzLThhM2EtNDVmYi1hNzllLTViM2IyNjI1NTEwMiIsImMiOjE3NTUyMzQ1NzY5NDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; IR_gbd=oppo.com; _fbp=fb.1.1755234576955.414896513993728546; _ga_DTXFPC1MML=GS2.1.s1755234576$o1$g1$t1755234581$j55$l0$h0; IR_15008=1755234582200%7C0%7C1755234582200%7C%7C; _hjSessionUser_2075538=eyJpZCI6IjU5ODJiODI0LTAxOWYtNTA1ZC05ODRlLTllMWI4Y2YxMzZhMiIsImNyZWF0ZWQiOjE3NTUyMzQ1NzY5NDUsImV4aXN0aW5nIjp0cnVlfQ==',
}

for i in zip_list:


    json_data = {
        'productType': 1,
        'pinCode':f'{i}',
        'skuItems': [
            {
                'skuCode': '5011100260',
            },
            {
                'skuCode': '5011100261',
            },
            {
                'skuCode': '5011100262',
            },
            {
                'skuCode': '5011100263',
            },
            {
                'skuCode': '5011100264',
            },
            {
                'skuCode': '5011100265',
            },
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
    print(f'Response of zipcode{i}',response.status_code)

    data=json.loads(response.text)
    # print(data)

    with open(f'D:\madri_new_codes\oppo\saved_json\pincode_{i}.json','w',encoding='utf-8') as f:
        f.write(response.text)

    service_availability = 0 if data.get('data') is None else 1
    print(f'Service availability: {service_availability}')
    # cod_availability=data['data']['skuDetailShippingInfoMap']['5011100260'][0]['shippingMethodCode']
    # print(cod_availability)

    # cod_availability = 1 if data['data']['skuDetailShippingInfoMap']["5011100260"][0]['shippingMethodCode'] == "BlueDart-COD" else 0
    # print(cod_availability)

    cod_availability = 0  # default
    sku_map = None

    if data.get('data') and data['data'].get('skuDetailShippingInfoMap'):
        sku_map = data['data']['skuDetailShippingInfoMap']
        if "5011100260" in sku_map and sku_map["5011100260"]:
            if sku_map["5011100260"][0].get('shippingMethodCode') == "BlueDart-COD":
                cod_availability = 1


    # data['data']['skuDetailShippingInfoMap'][5011100263][0].shippingMethodCode']

    results.append(
        {
            'pincode': i,
            'Product_url':product_url,
            'service_availability': service_availability,
            'cod_availability': cod_availability
        })
output_df = pd.DataFrame(results)
print(output_df)

oppo_output_csv='D:\madri_new_codes\oppo\oppo_output_csv\oppo_output_csv.csv'
output_df.to_csv(oppo_output_csv,index=False)

