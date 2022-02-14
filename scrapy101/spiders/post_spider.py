from scrapy import Spider
from scrapy101.items import QuoteItem
class PostSpider(Spider):
    name = "posts"
    
    start_urls = [
         'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = QuoteItem()
            quote_item['author'] = quote.xpath('span/small/text()').extract()
            /html/body/div/div[2]/div[1]/div[9]/span[2]/a
            quote_item['author_link'] = quote.css('span a::attr("href")').get()
            quote_item['text'] = quote.css('span.text::text').extract()
            quote_item['text'] = quote.css('a.tag::text').extract()

            yield quote_item

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)