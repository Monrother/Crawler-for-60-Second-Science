import scrapy

class ScientificScrapy(scrapy.Spider):
    name = "Scientific"

    start_urls = ['https://www.scientificamerican.com/podcast/60-second-science/']

    def parse(self, response):
        for mp3_link in response.css(".podcasts-listing__download a::attr(href)").getall():
            yield(scrapy.Request(mp3_link, callback=self.parse_mp3))

    def parse_mp3(self, response):
        if 'Content-Disposition' in response.headers:
            Content_Disposition = response.headers['Content-Disposition'].decode("utf-8")
            ind = Content_Disposition.find("filename")
            file_name = Content_Disposition[ind + len("filename=\""):-1]
            with open(file_name, 'wb') as f:
                f.write(response.body)
            print("file saved to %s" % (file_name))
        
