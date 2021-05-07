from django.contrib import admin
from . import models
# Register your models here.

class ScrapyItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.ScrapyItemModel)
