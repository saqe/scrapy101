from scrapy import Spider

class PostSpider(Spider):
    name = "posts"
    
    start_urls = [
         'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        print(response)
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)