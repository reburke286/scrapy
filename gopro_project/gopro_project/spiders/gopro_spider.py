import scrapy


class GoProSpider(scrapy.Spider):
    name = "gopro"
    start_urls = [
        'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&amp&keywords=gopro+fusion&amp&qid=1550442454&amp&s=electronics&amp&sprefix=GoPro+Fu%2Celectronics%2C1332&amp&sr=1-3',
    ]

    def parse(self, response):
        # defining some variables before the yield that need to be further manipulated
        source = response.css('title::text').get()
        prod_name = response.css('#productTitle::text').get()
        full_list = response.css(
            '#feature-bullets span.a-list-item::text').getall()
        updated_list = full_list[2:]

        # yielding an object of the information
        yield {
            'prod_name': prod_name.strip(),
            'brand': response.css('.a-spacing-micro tr.a-spacing-small td.a-span9 span::text')[0].get(),
            'source': source.split()[0],
            'list_price': response.css('.a-lineitem td.a-span12 span::text')[0].get(),
            'description': updated_list,
            'review': response.css('#acrPopover a span::text').get(),
            'num_reviews': response.css('#acrCustomerReviewText::text').get()
        }

# in python terminal run scrapy crawl gopro -o info.json
# this will put a json file of the above information in the root folder
