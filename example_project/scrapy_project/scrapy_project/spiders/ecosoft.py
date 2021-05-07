import scrapy
from scrapy import Item, Field

from loginform import fill_login_form
from scrapy.http import FormRequest
from scrapy.http.request import Request
import logging
from scrapy import Selector
from selenium import webdriver
from scrapy.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..items import ScrapyProjectItem

class EcosoftSpider(scrapy.Spider):
    name = 'ecosoft'
    # allowed_domains = ['www.ecosoftbd.com']
    start_urls = ['https://ost.ecosoftbd.com/Login']

    # def __init__(self,*args,**kwargs):
    #     self.url = kwargs.get("url")
    #     self.domain = kwargs.get('domain')
    #     self.start_urls = [self.url]
    #


    def parse(self, response, **kwargs):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path='./scrapy_project/geckodriver', options=options)
        driver.get(self.start_urls[0])
        driver.find_element_by_id("LoginId").send_keys("arif0171")
        driver.find_element_by_id("Password").send_keys("12341234")
        driver.find_element_by_class_name("button.login.t-button.btn-primary").click()
        driver.save_screenshot("test.png")
        # driver.find_element_by_id("SharePriceGrid").text
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Trading Code")))

        selx = Selector(text=driver.page_source, type="html")
        driver.close()
        def generate_item(fields):
            item = Item()
            for f in fields:
                item.fields[f] = Field()
            return item

        def whitespace(li):
            for item in li:
                if item == ' ':
                    return
                else:
                    return item

        fields = ["sn", "trade_code", "cat", "ltp", "change",
                  "change_persent", "value", "volume", "trade", "high",
                  "low", "open", "ycp"]
        for sel in selx.css('table > tbody > tr'):
            # print(len(sel),'xxxxx\n\n\n\n\n\nxxxxxxx')//NO LENGTH
            item_instance = ScrapyProjectItem()
            # data = {}
            data = sel.css('::text').getall() # get() td::text not work # print(sel.css('tr.t-alt >td::text').getall()) # not work properly
            data1 = sel.css('td.span::text').getall() # get() td::text not work # print(sel.css('tr.t-alt >td::text').getall()) # not work properly
            # print("dataxx", ' xx' , data)
            print('LENGTH OF DATA', len(data))
            l = list(filter(whitespace, data))

            if l[0].isdigit() and (len(l)>14 and len(l) <18) :
                print('llllllllllll',l)
                print(len(l), '\n')
                item_instance['sn'] = l[0]
                item_instance['trade_code'] = l[1]
                item_instance['cat'] = l[2]
                item_instance['ltp'] = l[3]
                item_instance['change'] = l[4]
                item_instance['change_persent'] = l[5]
                item_instance['value'] = l[6]
                item_instance['volume'] = l[7]
                item_instance['trade'] = l[8]
                item_instance['high']= l[9]
                item_instance['low'] = l[10]
                item_instance['open'] = l[11]
                item_instance['ycp'] = l[12]
            yield item_instance




