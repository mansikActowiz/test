import scrapy
from scrapy.cmdline import execute
from scrapy.http import Response
import json
import csv
import pprint

class ImdbTopSpider(scrapy.Spider):
    name = "imdb_top_single"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'ROBOTSTXT_OBEY': False  # Optional: disable robots.txt rule
    }

    def parse(self, response):
        # Print the class variables here
        print(f"Spider name: {self.name}")
        print(f"Allowed domains: {self.allowed_domains}")
        print(f"Start URLs: {self.start_urls}")


        # title = response.xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base"]//h3[@class="ipc-title__text"]/text()').getall()
        # print(title)
        # # new_title=response.xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base"]//h3[@class="ipc-title__text"]/text()').getall()
        # # print(new_title)
        # year=response.xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base"]//span[@class="sc-4b408797-8 iurwGb cli-title-metadata-item"]/text()').getall()
        # print(year)
        # release_year=year[0::3]
        # print(release_year)
        # duration=year[1::3]
        # print(duration)
        # rating=response.xpath('//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base"]//span[@class="sc-4b408797-2 icoKEg"]//div[@class="sc-bfa1b6a1-0 ezSnho sc-4b408797-3 btDxPM cli-ratings-container"]//span[@class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"]//span[@class="ipc-rating-star--rating"]/text()').getall()
        # print(rating)
        #

        print('********************************************************')



        json_path=response.xpath('//script[@type="application/ld+json"]/text()').getall()
        print(len(json_path)) #1
        print(json_path) #this will come inside list[{}]
        json_path=json_path[0] #taking 1st part of list so it becomes dictionary only.it will com as {}
        print(json_path)

        json_data=json.loads(json_path)
        print(json_data) #152831 dictionaries
        print('json data /////////////////////////////////////')
        print(len(json_data))

        name=json_data['itemListElement'][1]['item']['name']
        print('name',name)
        # itemListElement[1].item.image
        image=json_data['itemListElement'][1]['item']['image']
        print('image',image)
        url_path=json_data['itemListElement'][1]['item']['url']
        print(url_path)

        rating=json_data['itemListElement'][1]['item']['aggregateRating']['ratingValue']
        print('rating',rating)
        duration = json_data['itemListElement'][1]['item']['duration']
        duration = duration[2:]
        print('duration',duration)




if __name__ == '__main__':
        execute(f'scrapy crawl imdb_top_single'.split())




