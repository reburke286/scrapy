import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings


class GoProSpider(scrapy.Spider):
    name = "gopro"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&amp&keywords=gopro+fusion&amp&qid=1550442454&amp&s=electronics&amp&sprefix=GoPro+Fu%2Celectronics%2C1332&amp&sr=1-3',
    ]

    custom_settings = {
        'ITEM_PIPELINES': {'gopro_project.pipelines.InfoPipeline': 300, }
    }

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


class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",

    ]

    custom_settings = {
        'ITEM_PIPELINES': {'gopro_project.pipelines.ReviewsPipeline': 300, }
    }

    def parse(self, response):
        review_id = response.css("div.aok-relative::attr(id)").extract()
        title = response.css(".review-title span::text").extract()
        date = response.css(
            "div.aok-relative span.review-date::text").extract()
        rating = response.css(
            ".review-views .review-rating span.a-icon-alt::text").extract()
        # need to figure out why I can't get text after <br>
        text = response.css("span.review-text-content span::text").extract()
        for info in zip(review_id, title, date, rating, text):
            scraped_info = {
                'review_id': info[0],
                'title': info[1],
                'date': info[2],
                'rating': info[3],
                'text': info[4]
            }

            yield scraped_info
        next_page = response.css(
            '#cm_cr-pagination_bar li.a-last a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        elif next_page is None:
            print(next_page)


# settings = get_project_settings()
process = CrawlerProcess(get_project_settings())
process.crawl(GoProSpider)
process.crawl(ReviewsSpider)
process.start()
