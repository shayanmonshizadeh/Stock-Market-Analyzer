import scrapy


class WSJSpider(scrapy.Spider):
    name = "WSJ"

    start_urls = [
        'http://wsj.com'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
