# encoding:utf-8
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import random
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Q
#sssss

def index(request):
    news = News.objects.all().order_by("dimDate")
    news = news[0:4]
    return  render(request,'index.html',locals())


def news(req):
    news=News.objects.all()
    return render(req,'news.html',locals())


def newsdetail(req,id=0):

    news=News.objects.filter(id=id)
    try:
        n=news[0]
    except:
        return Http404()
    return render(req,'newsdetail.html',locals())

