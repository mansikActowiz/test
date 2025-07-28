import requests
import random
import gzip
from parsel import Selector
import json
import csv
import pandas as pd
from sqlalchemy import create_engine
import requests
import random


url='https://www.viator.com/tours/Asheville/Half-Day-Waterfall-Tour/d22561-67706P3'



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



cookies = {
    'x-viator-tapersistentcookie': '1f5b6c9d-4e0e-4adb-9a5c-65aa8f48012f',
    'x-viator-tapersistentcookie-xs': '1f5b6c9d-4e0e-4adb-9a5c-65aa8f48012f',
    'SEM_PARAMS': '%7B%7D',
    'EXTERNAL_SESSION_ID': '',
    'XSRF-TOKEN': '254ea5c1-f133-4d17-81fe-0ce66825b0e3',
    '_gcl_au': '1.1.1687995617.1748517136',
    'OptanonAlertBoxClosed': '2025-05-29T11:12:48.441Z',
    'SEM_MCID': '42385',
    'LAST_TOUCH_SEM_MCID': '42385',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+May+29+2025+17%3A49%3A38+GMT%2B0530+(India+Standard+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e422d62a-cc4a-46af-8c8f-35916d9b6a8f&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=US%3BNY&AwaitingReconsent=false',
    'profilingSession': '8%252B177YMAIcrtLa%252BXh3vz0g%253D%253D%257CKEbw9HMcklJBQUCkN%252B7yD7nLw%252B1qfXwpA5e5rGulSZcByFXstNw3vIwvzb9%252FBy1Gxk0PE%252Byq2ufjndQ%252BPWm8EGmy290Je3VE%252Fak8DrKmHpB12Q%253D%253D%257CF4rxjotg%252BPw%253D%253A8BKxUHp4p%252FeBM2D5PFjlftqh3HNufLyKVeALqJtqTIk%253D',
    'ORION_SESSION': 'p57wv2X2wVur56%2Bg2jDkZg%3D%3D%7CL1Jtyrc%2FvddQ9%2Fypa3xXa%2Bn04brBd1BxwfkMEo38rAemkAyD9IdVUG1s5uA4Non0sBwTM4N%2FBI2KvMA%2B0chL09%2FCVJL9Kqs1a2UhNinC6Oa4Qo8RWqE8b7IWIKy2Mj3qlZsN9aGz%2BenbQ1GGZIKj%2FdOzfnkR296KhfdxCBkGxSDyXyzrR1svM4n5xGuapkbV5ILIIaGpsuPQbXfcK3aKx1kvbuqEyJyNOK4tV9C%2BD03FrzR0rc5kKvV2V9iUR9MudWGmdQNbPK3j6AkuXsbpBSgF9LT7GbHB1GTeTLaSU9KBcTEI2kTi1eB3iSj2iJNp5vo77Z5%2BcwlEU9UB9lSpar6vDaeJw3NsoO7zzkxydj49usAuhH9hKY%2BuD2%2BBKct1rmXDFhYaf7RfeOQe%2BIPNUizrGiA6ll%2BPhbmOw%2Fm4dlPrYBIkj2IHB5w%2BF8wLeDYphfRHZXFi7u%2FNwabtL%2FeOkBC0lFNTDIRKp6YB%2B9Po3I%2BYmJeCg79FvH69lMTeMsTzayURIXYobVSaz5MZYDI1FtCJuzZsDBVQaafRp9TNb9NK5%2BVV5jh2M2rivIDTkaiovEJnMk9cVPcdtmrJWujlU2XqB6Ezr8SXeJW7W8DPLI3%2BVTMsPbVz%2BiEOKA2%2BIdHLBEJIVZYMoYsSjEVd0ox1FKtrPcSLmP4ilAcNLpvBflgrs%2BBXSKKP%2Frk4iXAZM8K3IlUxHu4ekmrteyWsnRW0duRqNY4KPxKkzZMgepPbfz%2FwTWy2GZnYmwTLbBrlT9IiXJbGaGwmVVqE2fV%2BSHYcnrotXBp360r%2BWxuFjpnTlC1PNwpnl59hYZIqajqhus1iJqPSxNUVKta9KZ2JoCHe20A6DUecK3PZbTomPzzC6EwSGPcgPVLqpz4eoHuaiezR1lryN1J99sPSaGgRIVYJUOLsOFjhjpy%2BSgiQfm468DkjzYYHWegrUbSjp6iB%2BsJ1CZKMepF3OCJtZavbjtohkkqCXTQUYLAWijqkMyY4mJya8wU9FP7WxVNkUm6uGDMehx3S1WK7n138IuYDr%2F8qJ76gxqOTGDtEatiOzSCJc15QXOF%2FR6B33PcjHhlbuuj%2Brktf7ea8fBMeN9gocjnZXR2MknObEs8NBqaTmsNun%2Bx2x3KqPtW7hrv20cpxHOk8AvMvMjoXC72ZFFlAbDgZAHLcqEbHZhu0EmSX8jWcqf%2FQW8p1LaV3ExqPlDotSQsIIe246GIAHKN%2BYuc%2FRHn7nz332JDzRQSxfpk%2BOkuZxUEn%2BsMtdxphtB4UNH5nqXLoxNfs29m5KV0vxI9A5Sj9MXELIo6TAzgg5PYUVTJwJ7nu5D%2FXLxUY36fLq%2BuLRgkRHYrF5pYsjenbSv9hYZLW3lYeZ87lMk57y3Au8%2B994r9ZPJWXpAeJGQ9Ei3IC%2F%2BwXy3NfCs1%2BCxMsTKuFDTCfekMz3T5ptMGb9XuF8nE%2BGuEfqX%2BKEp1wpyn3BRXpu9N5wGUnTIM%2Fb40Hp1RShbHsSR1Cl5WeBVtImhh6szvxN3SCiF5dOuVQ1IlIbzlAI%2BroFZttGCaMQoTsPJ5GEfbd1kQu9ze71wPKxtWDqXJRc3tVkEtbrAh%2FTi8Wtlr9X7RRS78V%2BZ7gP%2FKo8dj2PCgFtU8Ud%2BCq0uruZ19TcNrRFVks3tDdC%2FiD2rXJ%2FUN95UGRCFxaEB1iXrjbRIwsdExQhFRaZRGBKNHSn6RNp9I1X%2Fal6cQsqpeXxGbaIcbPyvY90Oc9fIPoP3ff6WvQjdeQ054XgaQEHWYX7%2BAnR13Tn%2BtDlsdzH9%2Fe4L28aGNgv%2FKAFDBVDszT4bosZJD5CAuOkOQEcJDvt4E6OONGRIzRC67LNT96ai81MpFQpwaV3EGs3NbAp4wucXB9Ed7sTnVLsmXi7zVE9V%2F%2BAncMh1DGGkR2CAznzZPbVWvtHnlEMMEwsflJl7srLJ85oywbY41oM5Tkuu4tttf%2F2VOIlRlFudtHzEstBggikhDGre3eloYWOAJKTy0%2Bx7BCqD4hgQCktrHNq8z4DrzcWEj2kxCLXhtMbPBYmGC7wCqHMv56z4LC7ongseNtkdSIol0XFldjbki1FvcGe7Lia%2BLXbutzaW%2FGRB3RpAs140hRp5gw9Cz1rW4SB0AQmQyQGw5Zjzs5eFiBYId42aDEUbf0QnGHlnnVUI04Rno9avlOLzGYtzIivvs42MkHVxNrRv1x4DdImykwHtGg5EABfn7eC64Z5dXKburN2UQj6R4PkRcMjEy5YZPonuHIPQ%3D%3D%7C%2FGA%2FOAPvMS4%3D%3AMFqPR4oZd8%2Bt8sXPaivmxdzCi4Zei%2BeUMzkdJz8l6pQ%3D',
    'ORION_SESSION_REQ': '9D347841%3A7066_0A2809E5%3A01BB_683850E7_12E61D5D%3A881EC%7C9D347841%3A7066_0A2809E5%3A01BB_683850C3_12E608BC%3A881EC%7C9D347841%3A7066_0A2809E5%3A01BB_683850E7_12E61D5D%3A881EC',
    'datadome': 'bR_JWUu~JoWjQNZYKOyJSiNOJu1sydUod2AEz~okcky9u0KhfuOpvQsrKBCG4U4Ob5uca7LeOpZ~652BmWB2DRsEZh3P2JTmh9Kq9a6jiBIQPdGtGCgamI_Pc_fN_J44',
    'REFERER_PAGE_REQUEST_ID': '9D347841:7066_0A2809E5:01BB_683850E7_12E61D5D:881EC',
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.viator.com',
    'priority': 'u=1, i',
    'referer': 'https://www.viator.com/tours/Asheville/Half-Day-Waterfall-Tour/d22561-67706P3',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Chromium";v="136.0.7103.114", "Google Chrome";v="136.0.7103.114", "Not.A/Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-442a4a8ad1fc9c5520e6e2abf225e058-93b679733476af96-01',
    'tracestate': 'es=s:0.1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-datadome-clientid': 'bR_JWUu~JoWjQNZYKOyJSiNOJu1sydUod2AEz~okcky9u0KhfuOpvQsrKBCG4U4Ob5uca7LeOpZ~652BmWB2DRsEZh3P2JTmh9Kq9a6jiBIQPdGtGCgamI_Pc_fN_J44',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': '254ea5c1-f133-4d17-81fe-0ce66825b0e3',
    # 'cookie': 'x-viator-tapersistentcookie=1f5b6c9d-4e0e-4adb-9a5c-65aa8f48012f; x-viator-tapersistentcookie-xs=1f5b6c9d-4e0e-4adb-9a5c-65aa8f48012f; SEM_PARAMS=%7B%7D; EXTERNAL_SESSION_ID=; XSRF-TOKEN=254ea5c1-f133-4d17-81fe-0ce66825b0e3; _gcl_au=1.1.1687995617.1748517136; OptanonAlertBoxClosed=2025-05-29T11:12:48.441Z; SEM_MCID=42385; LAST_TOUCH_SEM_MCID=42385; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+29+2025+17%3A49%3A38+GMT%2B0530+(India+Standard+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=e422d62a-cc4a-46af-8c8f-35916d9b6a8f&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=US%3BNY&AwaitingReconsent=false; profilingSession=8%252B177YMAIcrtLa%252BXh3vz0g%253D%253D%257CKEbw9HMcklJBQUCkN%252B7yD7nLw%252B1qfXwpA5e5rGulSZcByFXstNw3vIwvzb9%252FBy1Gxk0PE%252Byq2ufjndQ%252BPWm8EGmy290Je3VE%252Fak8DrKmHpB12Q%253D%253D%257CF4rxjotg%252BPw%253D%253A8BKxUHp4p%252FeBM2D5PFjlftqh3HNufLyKVeALqJtqTIk%253D; ORION_SESSION=p57wv2X2wVur56%2Bg2jDkZg%3D%3D%7CL1Jtyrc%2FvddQ9%2Fypa3xXa%2Bn04brBd1BxwfkMEo38rAemkAyD9IdVUG1s5uA4Non0sBwTM4N%2FBI2KvMA%2B0chL09%2FCVJL9Kqs1a2UhNinC6Oa4Qo8RWqE8b7IWIKy2Mj3qlZsN9aGz%2BenbQ1GGZIKj%2FdOzfnkR296KhfdxCBkGxSDyXyzrR1svM4n5xGuapkbV5ILIIaGpsuPQbXfcK3aKx1kvbuqEyJyNOK4tV9C%2BD03FrzR0rc5kKvV2V9iUR9MudWGmdQNbPK3j6AkuXsbpBSgF9LT7GbHB1GTeTLaSU9KBcTEI2kTi1eB3iSj2iJNp5vo77Z5%2BcwlEU9UB9lSpar6vDaeJw3NsoO7zzkxydj49usAuhH9hKY%2BuD2%2BBKct1rmXDFhYaf7RfeOQe%2BIPNUizrGiA6ll%2BPhbmOw%2Fm4dlPrYBIkj2IHB5w%2BF8wLeDYphfRHZXFi7u%2FNwabtL%2FeOkBC0lFNTDIRKp6YB%2B9Po3I%2BYmJeCg79FvH69lMTeMsTzayURIXYobVSaz5MZYDI1FtCJuzZsDBVQaafRp9TNb9NK5%2BVV5jh2M2rivIDTkaiovEJnMk9cVPcdtmrJWujlU2XqB6Ezr8SXeJW7W8DPLI3%2BVTMsPbVz%2BiEOKA2%2BIdHLBEJIVZYMoYsSjEVd0ox1FKtrPcSLmP4ilAcNLpvBflgrs%2BBXSKKP%2Frk4iXAZM8K3IlUxHu4ekmrteyWsnRW0duRqNY4KPxKkzZMgepPbfz%2FwTWy2GZnYmwTLbBrlT9IiXJbGaGwmVVqE2fV%2BSHYcnrotXBp360r%2BWxuFjpnTlC1PNwpnl59hYZIqajqhus1iJqPSxNUVKta9KZ2JoCHe20A6DUecK3PZbTomPzzC6EwSGPcgPVLqpz4eoHuaiezR1lryN1J99sPSaGgRIVYJUOLsOFjhjpy%2BSgiQfm468DkjzYYHWegrUbSjp6iB%2BsJ1CZKMepF3OCJtZavbjtohkkqCXTQUYLAWijqkMyY4mJya8wU9FP7WxVNkUm6uGDMehx3S1WK7n138IuYDr%2F8qJ76gxqOTGDtEatiOzSCJc15QXOF%2FR6B33PcjHhlbuuj%2Brktf7ea8fBMeN9gocjnZXR2MknObEs8NBqaTmsNun%2Bx2x3KqPtW7hrv20cpxHOk8AvMvMjoXC72ZFFlAbDgZAHLcqEbHZhu0EmSX8jWcqf%2FQW8p1LaV3ExqPlDotSQsIIe246GIAHKN%2BYuc%2FRHn7nz332JDzRQSxfpk%2BOkuZxUEn%2BsMtdxphtB4UNH5nqXLoxNfs29m5KV0vxI9A5Sj9MXELIo6TAzgg5PYUVTJwJ7nu5D%2FXLxUY36fLq%2BuLRgkRHYrF5pYsjenbSv9hYZLW3lYeZ87lMk57y3Au8%2B994r9ZPJWXpAeJGQ9Ei3IC%2F%2BwXy3NfCs1%2BCxMsTKuFDTCfekMz3T5ptMGb9XuF8nE%2BGuEfqX%2BKEp1wpyn3BRXpu9N5wGUnTIM%2Fb40Hp1RShbHsSR1Cl5WeBVtImhh6szvxN3SCiF5dOuVQ1IlIbzlAI%2BroFZttGCaMQoTsPJ5GEfbd1kQu9ze71wPKxtWDqXJRc3tVkEtbrAh%2FTi8Wtlr9X7RRS78V%2BZ7gP%2FKo8dj2PCgFtU8Ud%2BCq0uruZ19TcNrRFVks3tDdC%2FiD2rXJ%2FUN95UGRCFxaEB1iXrjbRIwsdExQhFRaZRGBKNHSn6RNp9I1X%2Fal6cQsqpeXxGbaIcbPyvY90Oc9fIPoP3ff6WvQjdeQ054XgaQEHWYX7%2BAnR13Tn%2BtDlsdzH9%2Fe4L28aGNgv%2FKAFDBVDszT4bosZJD5CAuOkOQEcJDvt4E6OONGRIzRC67LNT96ai81MpFQpwaV3EGs3NbAp4wucXB9Ed7sTnVLsmXi7zVE9V%2F%2BAncMh1DGGkR2CAznzZPbVWvtHnlEMMEwsflJl7srLJ85oywbY41oM5Tkuu4tttf%2F2VOIlRlFudtHzEstBggikhDGre3eloYWOAJKTy0%2Bx7BCqD4hgQCktrHNq8z4DrzcWEj2kxCLXhtMbPBYmGC7wCqHMv56z4LC7ongseNtkdSIol0XFldjbki1FvcGe7Lia%2BLXbutzaW%2FGRB3RpAs140hRp5gw9Cz1rW4SB0AQmQyQGw5Zjzs5eFiBYId42aDEUbf0QnGHlnnVUI04Rno9avlOLzGYtzIivvs42MkHVxNrRv1x4DdImykwHtGg5EABfn7eC64Z5dXKburN2UQj6R4PkRcMjEy5YZPonuHIPQ%3D%3D%7C%2FGA%2FOAPvMS4%3D%3AMFqPR4oZd8%2Bt8sXPaivmxdzCi4Zei%2BeUMzkdJz8l6pQ%3D; ORION_SESSION_REQ=9D347841%3A7066_0A2809E5%3A01BB_683850E7_12E61D5D%3A881EC%7C9D347841%3A7066_0A2809E5%3A01BB_683850C3_12E608BC%3A881EC%7C9D347841%3A7066_0A2809E5%3A01BB_683850E7_12E61D5D%3A881EC; datadome=bR_JWUu~JoWjQNZYKOyJSiNOJu1sydUod2AEz~okcky9u0KhfuOpvQsrKBCG4U4Ob5uca7LeOpZ~652BmWB2DRsEZh3P2JTmh9Kq9a6jiBIQPdGtGCgamI_Pc_fN_J44; REFERER_PAGE_REQUEST_ID=9D347841:7066_0A2809E5:01BB_683850E7_12E61D5D:881EC',
}
json_data = {
    'minShelfItems': 1,
    'shelfGroupType': 'PDP_AFFINITY_PRODUCTS',
    'shelfItemLimit': 9,
    'destinationId': 22561,
    'productCode': '67706P3',
}
response = requests.post('https://www.viator.com/tours/ajaxShelf', cookies=cookies, headers=headers, json=json_data)

print(response.status_code)



output_path = r'C:\Users\Madri.Gadani\Desktop\madri\viator\viator_html.html'
# output_path=r'C:\Users\Madri.Gadani\Desktop\madri\starbuck_saudiarabia\starbuck_saudiarabia_html.html'
print(output_path)

raw_html=response.text
print(raw_html)
print('//////////////////////////////')

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')


data = json.loads(raw_html)
print(data)
exit(0)
waterfall_tour = None
for item in data['items']:
    if item['data']['title'] == 'Waterfall Hike and Jeep Excursion - Waterfall Hiking Tour':
        waterfall_tour = item
        break

print(waterfall_tour)
print('3333333333333333')
if waterfall_tour:
    tour_info = {
        'title': waterfall_tour['data']['title'],
        'description': waterfall_tour['data']['description'],
        'url': waterfall_tour['data']['url'],
        'price': waterfall_tour['data']['price']['retailPrice']['amount'],
        'location': waterfall_tour['data']['location'],
    }
    print(tour_info)

target_title = "Waterfall"

# Example: If data is a list of tour dictionaries
for item in data:
    # Check if the title matches the one you want
    if 'title' in item and item['title'] == target_title:

        print("Code:", item.get('code', 'N/A'))
        print("Title:", item.get('title', 'N/A'))
        print("Price:", item.get('price', 'N/A'))
        # Print other parameters if exist
        for key, value in item.items():
            if key not in ['code', 'title', 'price']:
                print(f"{key}: {value}")
        break  # stop after finding the first matching item
else:
    print("Tour not found")

exit(0)

selector = Selector(text=raw_html)

script_tags = selector.xpath('//script[@type="application/ld+json"]/text()').getall()

title = None
code = None
price = None

for script_content in script_tags:
    try:
        data = json.loads(script_content.strip())
        if isinstance(data, dict) and data.get('@type') == 'Product':
            title = data.get('name')
            price = data.get('offers', {}).get('price')
            break
    except json.JSONDecodeError:
        continue

# Extract product code from the URL or from meta tags
product_code = url.split('-')[-1]  # '67706P3'

# Output
print("Title:", title)
print("Code:", product_code)
print("Price:", price)


page_title = selector.xpath('//title/text()').get()
print("Page Title:", page_title)
exit(0)

stores = selector.xpath('//div[@class="Teaser--nearby"]')
print(f"Found {len(stores)} stores on this page")


home_page = selector.xpath('//div[@class="Teaser--nearby"]')
print(len(home_page))

store_data=[]
for i in home_page:
    name =i.xpath('.//h2[@class="Teaser-title"]/text()').get()
    print('name', name)
    time=i.xpath('.//span[@class="Hours-statusText"]//text()').getall()
    print('time', time)
    add=i.xpath('.//div[@class="Teaser-address"]/text()').getall()
    print('add', add)
    direction=i.xpath('.//div[@class="c-get-directions-button-wrapper"]/a/@href').getall()
    print('direction', direction)
    # count = i.xpath('.//section[@class="Directory Directory--ace CityList"]//li[@class="Directory-listItem"]//a[@class="Directory-listLink"]//@data-count').getall()
    # print('count', count)

    # exit(0)
    store_dict={
        'name':name,

        'direction':direction,


    }
    store_data.append(store_dict)
print(store_data)
exit(0)
