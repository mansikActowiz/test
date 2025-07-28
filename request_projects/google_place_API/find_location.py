import requests
import gzip

from parsel import Selector

cookies = {
    '_fbp': 'fb.1.1753094242380.589335585774181527',
    '_gcl_au': '1.1.1026198639.1753094271',
    '_gid': 'GA1.2.140294239.1753094272',
    '__adroll_fpc': 'fa8cfbe03e8efd07aae5911289aca6f7-1753094275238',
    '__attentive_id': 'ad7612815036413fa888fd00120a4a85',
    '__attentive_cco': '1753094275615',
    'cmplz_banner-status': 'dismissed',
    '_attn_bopd_': 'none',
    '__attentive_session_id': '48fc01fa06c144e4a42c1e10891f8a0b',
    '__attentive_ss_referrer': 'ORGANIC',
    '__attentive_dv': '1',
    '_ga': 'GA1.1.456988012.1753094272',
    '__ar_v4': 'GVEFLS4XOFGQJCVBUG36UW%3A20250720%3A7%7CQ6ZVOEHX4JF2VBGU7S52DY%3A20250720%3A7',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzUzMDk0Mjc1NjEzLFwidW9cIjoxNzUzMDk0Mjc1NjEzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImFkNzYxMjgxNTAzNjQxM2ZhODg4ZmQwMDEyMGE0YTg1XCJ9Iiwic2VzIjoie1widmFsXCI6XCI0OGZjMDFmYTA2YzE0NGU0YTQyYzFlMTA4OTFmOGEwYlwiLFwidW9cIjoxNzUzMTU3OTk5MTc4LFwiY29cIjoxNzUzMTU3OTk5MTc4LFwibWFcIjowLjAyMDgzMzMzMzMzMzMzMzMzMn0ifQ==',
    '__attentive_pv': '4',
    '_ga_EDM93YPLD1': 'GS2.1.s1753155423$o2$g1$t1753158006$j49$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_fbp=fb.1.1753094242380.589335585774181527; _gcl_au=1.1.1026198639.1753094271; _gid=GA1.2.140294239.1753094272; __adroll_fpc=fa8cfbe03e8efd07aae5911289aca6f7-1753094275238; __attentive_id=ad7612815036413fa888fd00120a4a85; __attentive_cco=1753094275615; cmplz_banner-status=dismissed; _attn_bopd_=none; __attentive_session_id=48fc01fa06c144e4a42c1e10891f8a0b; __attentive_ss_referrer=ORGANIC; __attentive_dv=1; _ga=GA1.1.456988012.1753094272; __ar_v4=GVEFLS4XOFGQJCVBUG36UW%3A20250720%3A7%7CQ6ZVOEHX4JF2VBGU7S52DY%3A20250720%3A7; _attn_=eyJ1Ijoie1wiY29cIjoxNzUzMDk0Mjc1NjEzLFwidW9cIjoxNzUzMDk0Mjc1NjEzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImFkNzYxMjgxNTAzNjQxM2ZhODg4ZmQwMDEyMGE0YTg1XCJ9Iiwic2VzIjoie1widmFsXCI6XCI0OGZjMDFmYTA2YzE0NGU0YTQyYzFlMTA4OTFmOGEwYlwiLFwidW9cIjoxNzUzMTU3OTk5MTc4LFwiY29cIjoxNzUzMTU3OTk5MTc4LFwibWFcIjowLjAyMDgzMzMzMzMzMzMzMzMzMn0ifQ==; __attentive_pv=4; _ga_EDM93YPLD1=GS2.1.s1753155423$o2$g1$t1753158006$j49$l0$h0',
}

response = requests.get('https://pacificcatch.com/locations/', cookies=cookies, headers=headers)
print(response.status_code)

raw_html=response.text

output_path=r'C:\Users\Madri.Gadani\Desktop\madri\google_place_API\pacific\html\pacific_location.html'
gzip_output_path=r'C:\Users\Madri.Gadani\Desktop\madri\google_place_API\pacific\html\pacific_location_gzip.html'



with open(output_path, 'w', encoding='utf-8') as file:
    file.write(raw_html)
print("HTML content fetched and written successfully.")

with open(output_path, 'rb') as file_binary:
    with gzip.open(output_path + '.gz', 'wb') as file_gzip:
        file_gzip.writelines(file_binary)
print('file has been saved in compressed zip file.')


selector=Selector(text=raw_html)

locations = selector.xpath("//div[contains(@class, 'locations-grid__item')]")


location_lst=[]

for loc in locations:
    loc_name = loc.xpath(".//h2/text()").get(default='').strip()
    address_parts = loc.xpath(".//p/text()").getall()
    address = ' '.join(part.strip() for part in address_parts if part.strip())
    print(f"{loc_name} - {address}")
    location_lst.append(loc_name)
print("list of all locations:",location_lst)

API_KEY = "AIzaSyCFF3MgmVjgeFyrh7aHGFnAE8MJnAIK-WI"

for location in location_lst:
    print(location)

    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": f"Pacific Catch {location}",
        "inputtype": "textquery",
        "fields": "name,formatted_address,place_id,website,opening_hours,rating,url",
        "key": API_KEY
    }

    response = requests.get(base_url, params=params)
    print(response.status_code)
    print(response.url)
    data = response.json()
    print(data)
    exit(0)

#
# import requests
# locations = [
#     "Campbell", "Corte Madera", "Cupertino", "Dublin", "La Jolla",
#     "Mountain View", "Palo Alto", "San Mateo", "Santa Clara",
#     "Santa Monica", "SF 9th Avenue", "SF Chestnut St", "Sunnyvale",
#     "Tustin", "Walnut Creek"
# ]
#
# for loc in locations:
#     print(loc)
#     url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Pacific+Catch+{loc}&inputtype=textquery&fields=name,formatted_address,place_id,website,opening_hours,rating,url&key=MY_API_KEY"
#     response = requests.get(url)
#     print(response.status_code)
#     print(url)
#     print(response.json())
