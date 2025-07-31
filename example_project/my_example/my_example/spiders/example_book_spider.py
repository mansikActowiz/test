import scrapy
from scrapy.http import Response

class BooksSpider(scrapy.Spider):
    name = "books"

    # def start_requests(self):
    #     '''database code
    #     self.connenction=df.conn()
    #     '''


    start_urls = ['http://books.toscrape.com/']

    def parse(self, response: Response):
        print(f"Visiting page: {response.url}")

        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            availability = book.css('p.instock.availability::text').getall()[-1].strip()

            print(f"Found book: {title} | Price: {price} | Availability: {availability}")

            yield {
                'title': title,
                'price': price,
                'availability': availability,
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            print(f"Found next page: {next_page}")
            yield response.follow(next_page, self.parse)
        else:
            print("No more pages to scrape.")
