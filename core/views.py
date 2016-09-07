# encoding:utf-8
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
import random
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.db.models import Q


def index(request):
    news = News.objects.all()
    news = news[0:4]

    serverList = serverno.objects.all()
    serverList = serverList[0:6]
    try:
        ios = NewsImg.objects.filter(apktype__name='ios')[0]
    except:
        ios = None
    try:
        android = NewsImg.objects.filter(apktype__name='android')[0]
    except:
        android = None

    c = Carousel.objects.all()
    c = c[0:4]

    return render(request, 'index.html', locals())


def news(req):
    news = News.objects.all()
    # type='news'
    # try:
    #     apklink=NewsImg.objects.all()[0].apk.name[4:]
    # except:
    #     apklink=""

    serverList = serverno.objects.all()
    serverList = serverList[0:6]

    try:
        ios = NewsImg.objects.filter(apktype__name='ios')[0]
    except:
        ios = None
    try:
        android = NewsImg.objects.filter(apktype__name='android')[0]
    except:
        android = None
    return render(req, 'news.html', locals())


def activity(req):
    news = Activities.objects.all()
    type = 'act'
    try:
        apklink = NewsImg.objects.all()[0].apk.name[4:]
    except:
        apklink = ""
    return render(req, 'news.html', locals())


def newsdetail(req, id=0):
    serverList = serverno.objects.all()
    serverList = serverList[0:6]

    try:
        ios = NewsImg.objects.filter(apktype__name='ios')[0]
    except:
        ios = None
    try:
        android = NewsImg.objects.filter(apktype__name='android')[0]
    except:
        android = None

    news = News.objects.filter(id=id)
    try:
        n = news[0]
    except:
        return Http404()
    try:
        apklink = NewsImg.objects.all()[0].apk.name[4:]
    except:
        apklink = ""
    return render(req, 'newsdetail.html', locals())


def activitydetail(req, id=0):
    news = Activities.objects.filter(id=id)
    try:
        n = news[0]
    except:
        return Http404()
    try:
        apklink = NewsImg.objects.all()[0].apk.name[4:]
    except:
        apklink = ""
    return render(req, 'newsdetail.html', locals())
