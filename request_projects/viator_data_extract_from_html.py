
import json


raw_html_txt=r'C:\Users\Madri.Gadani\Desktop\madri\viator\viator_html_text.txt'

with open(raw_html_txt, 'r', encoding='utf-8') as f:
    content = f.read()


data = json.loads(content)
print(json.dumps(data, indent=4))


search_str='Waterfall Hike and Jeep Excursion'
for item in data["items"]:
    title = item['data']['title']


    if search_str in title:
        print('matched title:',{title})
        data_items=item['data']
        title= data_items['title']
        print('title',title)
        code=data_items['code']
        print('Code',code)
        img=data_items['image']['src']
        print('Image_src',img)
        rating=data_items['rating']['score']
        print('Rating',rating)
        review=data_items['rating']['reviewCount']
        print('ReviewCount',review)
        location=data_items['location']
        print('Location:',location)

        price=data_items['price']['retailPrice']['amount']

        print(f'RetailPrice:{price} $')

        discounted_price=data_items['price']['discountedPrice']['amount']
        print(f'Discounted_price:{discounted_price} $')
        discount_amount=data_items['price']['discountAmount']['amount']
        print(f'Discounted_Amount:{discount_amount}$')
        url=data_items['url']
        print('url:',url)
        geolocation=data_items['geolocation']
        print('geolocation',geolocation)
        break


