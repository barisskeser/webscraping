import scrapy
from ..items import ScrapingItem
from scrapy import Request
from urllib.parse import urlparse, urljoin
import time


class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['www.hurriyetemlak.com']
    start_urls = ['https://www.hurriyetemlak.com/istanbul-satilik/daire?page=1']

    def parse(self, response):

        for href in response.xpath("//div[@class='links']/a[@class='card-link']/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_page)

        """page_url = response.xpath("//link[@rel='canonical']/@href").extract()
        page_number = int(str(page_url)[60:].split("'")[0])

        if page_number < 1400:
            url = response.urljoin("https://www.hurriyetemlak.com/istanbul-satilik/daire?page=" + str(page_number + 1))
            yield scrapy.Request(url, self.parse)"""


    def parse_page(self, response):
        item = ScrapingItem()

        item['fiyat'] = response.xpath("//div[@class='right']/p[@class='fontRB fz24 price']/text()").extract()
        tablo = response.xpath("//div[@class='det-adv-info']/ul[@class='adv-info-list']/li/span/text()").extract()
        info = response.xpath("//div[@class='det-title-bottom']/ul[@class='short-info-list']/li/span/text()").extract()
        konum = response.xpath("//div[@class='det-title-bottom']/ul[@class='short-info-list']/li/text()").extract()


        item['il'] = konum[0] # ['\nİstanbul\n', '\nFatih\n', '\nŞehremini\n', 'Satılık', ' Daire']
        item['ilce'] = konum[1]
        item['mahalle'] = konum[2]
        item['m2'] = info[1].split(' ')[0] # '150 m'
        item['oda'] = info[0].split(' + ')[0] # '3 + 1'
        item['salon'] = info[0].split(' + ')[1] # '3 + 1'


        for i in range(len(tablo)):
            if i > 0:
                if tablo[i - 1] == "Banyo Sayısı":
                    item['banyo'] = tablo[i]

                elif tablo[i - 1] == "Kat Sayısı":
                    item['bina_kat'] = tablo[i]

                elif tablo[i - 1] == "Bina Yaşı":
                    item['bina_yas'] = tablo[i]

                elif tablo[i - 1] == "Bulunduğu Kat":
                    item['bulunan_kat'] = tablo[i]

                elif tablo[i - 1] == "Cephe ":
                    item['cephe'] = tablo[i]

                elif tablo[i - 1] == "Isınma Tipi":
                    item['isinma_tipi'] = tablo[i]

                elif tablo[i - 1] == "Konut Şekli":
                    item['konut_sekli'] = tablo[i]

                elif tablo[i - 1] == "Krediye Uygunluk":
                    item['krediye_uygun'] = tablo[i]

                elif tablo[i - 1] == "Site İçerisinde":
                    item['site_icinde'] = tablo[i]

                elif tablo[i - 1] == "Takas":
                    item['takas'] = tablo[i]

                elif tablo[i - 1] == "Tapu Durumu":
                    item['tapu_durum'] = tablo[i]

                elif tablo[i - 1] == "Yakıt Tipi":
                    item['yakit_tipi'] = tablo[i]

                elif tablo[i - 1] == "Yapı Tipi":
                    item['yapi_tipi'] = tablo[i]

        return item
