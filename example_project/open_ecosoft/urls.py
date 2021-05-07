from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('api/crawl/', views.crawl, name='crawl'),

]