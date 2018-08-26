# -*- coding: utf-8 -*-
from scrapy import Spider


class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['https://www.class-central.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            print("True")
        else:
            print("False")
