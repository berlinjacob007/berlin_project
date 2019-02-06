import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']
    start_urls = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']

    def parse(self, response):
	print '**********************************************'
        #print response.body
        print response.xpath('//ul[@class="meta-list"]/li[1]/text()').extract()[0].strip()         #date
        print response.xpath('//div[@class="pd-lr-10 span9"]/h1[1]/text()').extract()[0].strip()   #Discover your brillience
        print response.xpath('//div[@class="name"]/span[1]/text()').extract()[0].strip()           #emerging brillience
        #yield {
        #        'date': response.xpath('//ul[@class="meta-list"]/li[1]/text()').extract(),
        #       'event_name': response.xpath('//div[@class="pd-lr-10 span9"]/h1[1]/text()').extract(),
        #      'EB': response.xpath('//div[@class="name"]/span[1]/text()').extract(),
                }
        print '*************************************************'
