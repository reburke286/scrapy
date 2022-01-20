import scrapy


class GoProSpider(scrapy.Spider):
    name = "reviews"
    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    ]

    def parse(self, response):
        next_page = response.css(
            '#cm_cr-pagination_bar li.a-last a::attr(href)').get()
