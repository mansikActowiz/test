import requests

from bs4 import BeautifulSoup

# Step 1: Send a GET request to a webpage
url = 'https://quotes.toscrape.com'
response = requests.get(url)  # This is the GET request
print('response',response)#response <Response [200]>
# Step 2: Get the HTML response
html = response.text  # This contains the page content

title=response.xpath('//div[@class="quote"]/span[@class="text"]/text()')
author=response.xpath('//div[@class="quote"]/span/small[@class="author"]/text()')
tag=response.xpath('//div[@class="quote"]/div[@class="tags"]/a[@class="tag"]/text()')

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 4: Extract data (e.g., all quotes on the page)
quotes = soup.find_all('span', class_='text')
print('quotes',quotes)

for quote in quotes:
    print(quote.text)
