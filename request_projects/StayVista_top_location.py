import requests

from functions.create_request import check_response, save_html

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'origin': 'https://www.stayvista.com',
    'priority': 'u=1, i',
    'referer': 'https://www.stayvista.com/',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

response = requests.get('https://v3api.stayvista.com/api/navigation-links', headers=headers)
print(response.status_code)

check_response(response)

html_path = r'C:\Users\Madri.Gadani\Desktop\madri\stay_vista\stay_vista.html'

save_html(response,html_path)

data=response.json()
# print(data)

footer_sections = data['data']["sections"]['footer']
# print(footer_sections)

for section in footer_sections:
    if section['title'] == 'Top Locations':
        for item in section['items']:
            title = item['title']
            full_url = 'https://www.stayvista.com' + item['item_uri']
            print(f"{title}: {full_url}")
