from parsel import Selector
import re
# from request_projects.read_gzip_file import html_content

output_path=r'C:\Users\Madri.Gadani\Desktop\madri\costco\html_page_extraction\costco.html'
print(output_path)
with open(output_path, 'r', encoding='utf-8') as f:
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

