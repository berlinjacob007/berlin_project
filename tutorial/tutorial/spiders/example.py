import scrapy



class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']
    start_urls = ['https://allevents.in/new%20delhi/discover-your-brilliance/939513959466235']

    def parse(self, response):
         url = response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[2]/div/img/@data-original').extract()[0].strip() # FOR MAP
         #print url
         url =url.split('|')
         print latitude and longitude are,url[1]               
                
	
         yield {

                'event_name':response.xpath('//*[@id="event-detail-fade"]/div[1]/div[2]/h1/text()').get(),
                'time': response.xpath('//*[@id="event-detail-fade"]/div[1]/div[2]/ul/li[1]/text()').get(),
                'description':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[1]/div[2]/text()').getall(),
                'venu':response.xpath('/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/ul/li[3]/p/span[1]/text()').get() ,
                'fw':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[2]/div[2]/div[2]/div[3]/div/a/text()').get(),
                'image_lnk1':response.xpath('//*[@id="event-detail-fade"]/div[1]/div[1]/img/@src').extract(),
                'img_lnk2':response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[1]/div[1]/a/@data-image').extract(),
                

              }

                  #print '**********************************************'
                  #print response.body
                  #print response.xpath('//ul[@class="meta-list"]/li[1]/text()').extract(),
                  #print response.xpath('//div[@class="pd-lr-10 span9"]/h1[1]/text()').extract(),
                  #print response.xpath('//div[@class="name"]/span[1]/text()').extract(),
	          #print '**********************************************'
