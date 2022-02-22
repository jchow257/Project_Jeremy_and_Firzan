import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['https://www.google.com/']
    start_urls = ['https://www.google.com//']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link':x.xpath(newsel).extract_first()
            }
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse())