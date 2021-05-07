# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from django.core.exceptions import ObjectDoesNotExist

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from open_ecosoft.models import ScrapyItemModel

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        try:
            myItms = ScrapyItemModel.objects.get(sn=item['sn'])
            if myItms:
                print(('Item already exist'))
            return item
        except ObjectDoesNotExist:
            pass
        mymodels = ScrapyItemModel()
        mymodels.sn = item['sn']
        mymodels.trade_code = item['trade_code']
        mymodels.cat = item['cat']
        mymodels.ltp = item['ltp']
        mymodels.change = item['change']
        mymodels.change_persent = item['change_persent']
        mymodels.value = item['value']
        mymodels.volume = item['volume']
        mymodels.trade = item['trade']
        mymodels.high = item['high']
        mymodels.low = item['low']
        mymodels.open = item['open']
        mymodels.ycp = item['ycp']
        # mymodels.sn = item['pe']
        # mymodels.sn = item['spot']
        # mymodels.sn = item['sector']
        # mymodels.sn = item['record_date']
        # mymodels.sn = item['dividend']
        # mymodels.sn = item['analysis']
        mymodels.save()
        return item
