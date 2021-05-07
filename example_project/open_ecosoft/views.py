from django.shortcuts import render

# Create your views here.

from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
# from .utils import URLUtil
# from .models import ScrapyItem
from . import models
# connect scrapyd service
scrapyd = ScrapydAPI('http://localhost:6800')

def index(request):
    latest_question_list = models.ScrapyItemModel.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'open_soft/index.html', locals())
