import scrapy



class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']
    start_urls = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']

    def parse(self, response):
                
                
	
        yield {

                'event_name':response.xpath('//*[@id="event-detail-fade"]/div[1]/div[2]/h1/text()').get(),
                'time': response.xpath('//*[@id="event-detail-fade"]/div[1]/div[2]/ul/li[1]/text()').get(),
                'description':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[1]/div[2]/text()').getall(),
                'venu':response.xpath('/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/ul/li[3]/p/span[1]/text()').get() ,
                'fw':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[2]/div[2]/div[2]/div[3]/div/a/text()').get(),
                'img_lnk1':response.xpath('//*[@id="event-detail-fade"]/div[1]/div[1]/img/@src').extract(),
                'img_lnk2':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[1]/div[1]/img/@src').extract(),
                

              }

