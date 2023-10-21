# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:02:19 2023

@author: jksls
"""

import scrapy
import pandas as pd


class KolesaSpider(scrapy.Spider):
    
    name = "kolesa"
    allowed_domains = ["kolesa.kz/"]
    start_urls = ["https://kolesa.kz/cars/"] #https://kolesa.kz/

    custom_settings={
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }

    def parse(self, response):
        car_listings = response.css(".a-el-info")

        for car_listing in car_listings:
            item = KolesaCarItem()
            item["make"] = car_listing.css(".a-el-info-title::text").get()
            item["model"] = car_listing.css(".a-el-info-motors::text").get()
            item["price"] = car_listing.css(".a-el-info-price::text").get()

            yield item

        # Follow pagination links if available
        next_page = response.css(".a-pagination-next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            