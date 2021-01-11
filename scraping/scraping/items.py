# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#Verileri tutmak için alanlar
class ScrapingItem(scrapy.Item):
    banyo = scrapy.Field()
    bina_kat = scrapy.Field()
    bina_yas = scrapy.Field()
    bulunan_kat = scrapy.Field()
    cephe = scrapy.Field()
    fiyat = scrapy.Field()
    il = scrapy.Field()
    ilce = scrapy.Field()
    isinma_tipi = scrapy.Field()
    konut_sekli = scrapy.Field()
    krediye_uygun = scrapy.Field()
    m2 = scrapy.Field()
    mahalle = scrapy.Field()
    oda = scrapy.Field()
    salon = scrapy.Field()
    site_icinde = scrapy.Field()
    takas = scrapy.Field()
    tapu_durum = scrapy.Field()
    yakit_tipi = scrapy.Field()
    yapi_tipi = scrapy.Field()
