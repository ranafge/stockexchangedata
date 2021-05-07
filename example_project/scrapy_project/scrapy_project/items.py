# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# fields = ["sn", "trade_code", "cat", "ltp", "change", "change_persent", "value", "volume", "trade", "high",
#           "low", "open", "ycp"]
#
# class MyItem(scrapy.Item):
#     def __init__(self):
#         for f in fields:
#             self.__dict__[f] = scrapy.Field()

# my_item = MyItem()
from scrapy import Item
from collections import OrderedDict
import six
class OrderedItem(Item):
    def __init__(self, *args, **kwargs):
        self._values = OrderedDict()
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v
class ScrapyProjectItem(scrapy.Item):
    sn = scrapy.Field()
    trade_code = scrapy.Field()
    cat = scrapy.Field()
    ltp = scrapy.Field()
    change = scrapy.Field()
    change_persent = scrapy.Field()
    value = scrapy.Field()
    volume = scrapy.Field()
    trade = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    open = scrapy.Field()
    ycp = scrapy.Field()
    # pe = scrapy.Field()
    # spot = scrapy.Field()
    # sector = scrapy.Field()
    # recode_date = scrapy.Field()
    # divident_info = scrapy.Field()
    # analysis_done_at = scrapy.Field()

#
# from scrapy import Item, Field
#
# fields = ["sn","trade_code","cat","ltp","change","change_persent","value","volume","trade","high","low"
# ,"open","ycp"]
#
# def generate_item(fields):
#     item = Item()
#     for f in fields:
#         item.fields[f] = Field()
#     return item
#
# item_instance = generate_item(fields)
# item_instance['sn'] = 'some_value'
# item_instance['trade_code'] = 12
# print(item_instance)