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
import urllib.parse
import urllib.request
import http.client as httplib

def my_custom_sql(sql,*para):
    cursor = connection.cursor()

    cursor.execute(sql,*para)

    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchall()

    return row