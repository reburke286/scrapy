import scrapy


class ReviewsSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",

    ]

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
