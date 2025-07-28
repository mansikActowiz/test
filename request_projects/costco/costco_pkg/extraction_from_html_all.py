from parsel import Selector
import re
import os
import json



output_path=r'C:\Users\Madri.Gadani\Desktop\madri\costco\html_page_extraction'

html_lst=os.listdir(output_path)
print(html_lst)

html_lst=[lst for lst in html_lst if lst.endswith ('.html')]
print(html_lst)

costco_all_lst=[]

for i in html_lst:
    print(i)
    abs_path=output_path+'/'+i
    print(abs_path)
    # exit(0)

    with open(abs_path, 'r', encoding='utf-8') as f:
        html_content=f.read()

    selector=Selector(text=html_content)


    title=selector.xpath('//div[@class="product-h1-container-v2 visible-lg-block visible-xl-block"]/h1/text()').get()
    print('title:',title)


    match = re.search(r"priceTotal:\s*initialize\(([\d.]+)\)", html_content)
    if match:
        price = match.group(1)
        print("Price:", price)
    else:
        print("Price not found")


    features=selector.xpath('//ul[@class="pdp-features"]//text()').getall()
    print('features:',features)
    cleaned_features = [item.strip() for item in features if item.strip()]

    for i, feature in enumerate(cleaned_features, 1):
        print(f"{i}. {feature}")


    img_link = selector.xpath('//img[@id="initialProductImageSticky"]/@src').get()
    print("Image Link:", img_link)

    costco_dict={
        'title':title,
        'price':price,
        'features':cleaned_features,
        'img_link':img_link,

    }
    costco_all_lst.append(costco_dict)
print(costco_all_lst)
json_path=r'C:\Users\Madri.Gadani\Desktop\madri\costco\costco_all_data_json.json'


with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(costco_all_lst, f, indent=4, ensure_ascii=False)

print("✅ JSON saved after full cleaning.")


