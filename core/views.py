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
from ThunderMovie.status import *
from ThunderMovie.douban import douban as doubanclass

def postBaiDu(filecontent, domain):
    URL = "/urls?site=www.dyhell.com&token=uUABfymakG1cPdbh"
    send_headers = {'Content-Type': 'text/plain'}
    conn = httplib.HTTPConnection("http://data.zz.baidu.com:80")
    # req = urllib2.Request(URL, data=data, headers=send_headers)
    conn.request(method="POST", url=URL, body=filecontent, headers=send_headers)
    response = conn.getresponse()
    baiduresult = response.read()
    conn.close()
    return baiduresult
def my_custom_sql(sql,*para):
    cursor = connection.cursor()

    cursor.execute(sql,*para)

    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchall()

    return row
def index(req):
    argGet = req.GET
    #films=FILM.objects.all().exclude(download_link=' \n')
    try:
        m_type = argGet.get('m_type', 'all')
        country = argGet.get('area', 'all')
        year = argGet.get('year', 'all')
        movietype = movie_type.get(m_type)
        moviearea = movie_area.get(country)
        movieyear = year

        if movietype != 0:
            films = FILM.objects.filter(tags=movietype)
        else:
            films = FILM.objects.all().exclude(download_link=' \n')

        if moviearea == 0:
            pass
        elif moviearea == 1:
            films = films.filter(~Q(film_country__icontains='大陆') & ~Q(film_country__icontains='美国') & ~Q(film_country__icontains='法国') & ~Q(film_country__icontains='英国') & ~Q(film_country__icontains='日本') & ~Q(film_country__icontains='韩国') & ~Q(film_country__icontains='印度') & ~Q(film_country__icontains='泰国')& ~Q(film_country__icontains='香港')& ~Q(film_country__icontains='台湾')& ~Q(film_country__icontains='德国'))
        else:
            films = films.filter(film_country__icontains=moviearea)

        if movieyear == 'all':
            pass
        if movieyear == '2016' or movieyear == '2015' or movieyear == '2014' or movieyear == '2013' or movieyear == '2012' or movieyear == '2011':
            films =films.filter(film_pub_year=movieyear)
        if movieyear == '10':
            films = films.filter(film_pub_year__gte=2000, film_pub_year__lte=2010)
        if movieyear == '90':
            films = films.filter(film_pub_year__gte=1990, film_pub_year__lte=1999)
        if movieyear == '80':
            films = films.filter(film_pub_year__gte=1980, film_pub_year__lte=1989)
        if movieyear == '70':
            films = films.filter(film_pub_year__gte=1970, film_pub_year__lte=1979)
        if movieyear == 'early':
            films = films.filter(film_pub_year__lt=1970)
        paginator = Paginator(films, 100)  # Show 5 contacts per page
        page = argGet.get('page')
        try:
            filmpaged = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            filmpaged = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            filmpaged = paginator.page(paginator.num_pages)

    except:
        page = 1
        return HttpResponse(page)
    return render(req,'index.html',locals())


def indextvseries(req):
    argGet = req.GET
    #tvseries=TVSERIES.objects.all().exclude(download_link=' \n')
    try:
        m_type = argGet.get('m_type', 'all')
        country = argGet.get('area', 'all')
        year = argGet.get('year', 'all')
        tvtype = tv_type.get(m_type)
        tvarea = tv_area.get(country)
        tvyear = year

        if tvtype != 0:
            tvseriess = TVSERIES.objects.filter(tags__contains=tvtype)
        else:
            tvseriess = TVSERIES.objects.all().exclude(download_link=' \n')

        if tvarea == 0:
            pass
        elif tvarea == 1:
            tvseriess = tvseriess.filter(~Q(tvseries_country__icontains='大陆') & ~Q(tvseries_country__icontains='美国') & ~Q(
                tvseries_country__icontains='法国') & ~Q(tvseries_country__icontains='英国') & ~Q(
                tvseries_country__icontains='日本') & ~Q(tvseries_country__icontains='韩国') & ~Q(
                tvseries_country__icontains='印度') & ~Q(tvseries_country__icontains='泰国') & ~Q(
                tvseries_country__icontains='香港') & ~Q(tvseries_country__icontains='台湾') & ~Q(tvseries_country__icontains='德国'))
        else:
            tvseriess = tvseriess.filter(tvseries_country__icontains=tvarea)

        if tvyear == 'all':
            pass
        if tvyear == '2016' or tvyear == '2015' or tvyear == '2014' or tvyear == '2013' or tvyear == '2012' or tvyear == '2011':
            tvseriess = tvseriess.filter(tvseries_pub_year=tvyear)
        if tvyear == '10':
            tvseriess = tvseriess.filter(tvseries_pub_year__gte=2000, tvseries_pub_year__lte=2010)
        if tvyear == '90':
            tvseriess = tvseriess.filter(tvseries_pub_year__gte=1990, tvseries_pub_year__lte=1999)
        if tvyear == '80':
            tvseriess = tvseriess.filter(tvseries_pub_year__gte=1980, tvseries_pub_year__lte=1989)
        if tvyear == '70':
            tvseriess = tvseriess.filter(tvseries_pub_year__gte=1970, tvseries_pub_year__lte=1979)
        if tvyear == 'early':
            tvseriess = tvseriess.filter(tvseries_pub_year__lt=1970)
        paginator = Paginator(tvseriess, 52)  # Show 5 contacts per page
        page = argGet.get('page')
        try:
            tvseriespaged = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tvseriespaged = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tvseriespaged = paginator.page(paginator.num_pages)
    except Exception as e:
        page=1
        return HttpResponse(e)
    return render(req,'indextvseries.html',locals())
@csrf_exempt
def gitpull(req):
    msg = os.popen('sudo sh /home/ubuntu/ThunderMovie/deploy.sh').read()
    return HttpResponse(json.dumps({'msg:': msg}))

def search(req):
    keywords = req.GET.get('key','')
    films=FILM.objects.filter(Q(film_intro__contains=keywords)|Q(film_name__contains=keywords)|Q(film_actors__contains=keywords)|Q(film_director__contains=keywords))
    tvseriess = TVSERIES.objects.filter(
        Q(tvseries_intro__contains=keywords) | Q(tvseries_name__contains=keywords) | Q(tvseries_actors__contains=keywords) | Q(
            tvseries_director__contains=keywords) | Q(tags__contains=keywords))

    #|Q(tags__tag_name__contains=keywords)
    return render(req, 'about.html', locals())
def post(url, data):#封装post方法
    s=urllib.request.Request(url, urllib.parse.urlencode(data).encode('utf-8'))
    #s.headers={}
    # s.urlopen().read()
    s.add_header('Content-Type', 'text/plain')
    #s.add_header('Content-Type', 'text/plain')
    return  urllib.request.urlopen(s).read().decode()

def single(req,fid=0):
    try:
        film=FILM.objects.get(id=fid)

        tags=film.tags.all()
        film.download_link = [tuple(x.split(',')) for x in film.download_link.split('\n')]
        return render(req,'single.html',locals())
    except Exception as e:
        return HttpResponseNotFound()
def singletvseries(req,fid=0):
    try:
        tvseries=TVSERIES.objects.get(id=fid)
        tags=tvseries.tags.split(' ')
        tvseries.download_link = [tuple(x.split(',')) for x in tvseries.download_link.split('\n')]
        return render(req,'singletvseries.html',locals())
    except Exception as e:
        return HttpResponseNotFound()

def randomdy(req):
    films=FILM.objects.all().exclude(download_link=' \n')
    ran=random.randint(0,len(films)-50)
    films = films[ran:50+ran]

    return render(req, 'randomdy.html', locals())


def homepage(request):
    films = FILM.objects.all()[:7]
    newfilmd = FILM.objects.all()[:8]
    return render(request, 'Home.html', locals())


def sitemap(req):
    sitemaplist=['www.dyhell.com','www.dyhell.com/random','www.dyhell.com/movies']
    films=FILM.objects.all()
    tvs=TVSERIES.objects.all()
    for film in films:
        sitemaplist.append('www.dyhell.com/movie/'+str(film.id))
    for tv in tvs:
        sitemaplist.append('www.dyhell.com/tv/' + str(tv.id))

    try:
        f=open('core/static/sitemap.txt', 'w')
        fsh=open('curlbaidu.sh', 'w')
        for line in sitemaplist:
            f.write(line+"\n")
            fsh.write(
                " curl -H 'Content-Type:text/plain' --data-binary %s 'http://data.zz.baidu.com/urls?site=www.dyhell.com&token=uUABfymakG1cPdbh' \n" % line)
            fsh.write(
                " curl -H 'Content-Type:text/plain' --data-binary %s 'http://data.zz.baidu.com/update?site=www.dyhell.com&token=uUABfymakG1cPdbh' \n" % line)
        f.close()
        fsh.close()
        #msg=os.popen('sudo sh curlbaidu.sh').read()
    except Exception as e:
        return  HttpResponse(e)
    return HttpResponse('成功更新\n')#+msg)
def seolist(req):
    argGet = req.GET
    # films=FILM.objects.all().exclude(download_link=' \n')
    try:
        m_type = argGet.get('m_type', 'all')
        country = argGet.get('area', 'all')
        year = argGet.get('year', 'all')
        movietype = movie_type.get(m_type)
        moviearea = movie_area.get(country)
        movieyear = year

        if movietype != 0:
            films = FILM.objects.filter(tags=movietype)
        else:
            films = FILM.objects.all().exclude(download_link=' \n')

        if moviearea == 0:
            pass
        elif moviearea == 1:
            films = films.filter(~Q(film_country__icontains='大陆') & ~Q(film_country__icontains='美国') & ~Q(
                film_country__icontains='法国') & ~Q(film_country__icontains='英国') & ~Q(
                film_country__icontains='日本') & ~Q(film_country__icontains='韩国') & ~Q(
                film_country__icontains='印度') & ~Q(film_country__icontains='泰国') & ~Q(
                film_country__icontains='香港') & ~Q(film_country__icontains='台湾') & ~Q(film_country__icontains='德国'))
        else:
            films = films.filter(film_country__icontains=moviearea)

        if movieyear == 'all':
            pass
        if movieyear == '2016' or movieyear == '2015' or movieyear == '2014' or movieyear == '2013' or movieyear == '2012' or movieyear == '2011':
            films = films.filter(film_pub_year=movieyear)
        if movieyear == '10':
            films = films.filter(film_pub_year__gte=2000, film_pub_year__lte=2010)
        if movieyear == '90':
            films = films.filter(film_pub_year__gte=1990, film_pub_year__lte=1999)
        if movieyear == '80':
            films = films.filter(film_pub_year__gte=1980, film_pub_year__lte=1989)
        if movieyear == '70':
            films = films.filter(film_pub_year__gte=1970, film_pub_year__lte=1979)
        if movieyear == 'early':
            films = films.filter(film_pub_year__lt=1970)
        filmpaged = FILM.objects.all().exclude(download_link=' ')

    except:
        page = 1
        return HttpResponse(page)

    return render(req,'index.html',locals())

def douban(req, start ,end):
    '''
    id  from 18387 to 29120
    :param request:
    :return:
    '''
    try:
        for i in range(int(start), int(end)+1):
            film = FILM.objects.get(id=i)
            if film:
                db = doubanclass()
                douban_id = db.get_film_douban_id(film.film_name, film.film_pub_year)
                if douban_id == "":
                    return  HttpResponse('未从' + film.film_name + '，电影id:' + str(film.id) + '获取豆瓣id')
                while douban_id == "error":
                    douban_id = db.get_film_douban_id(film.film_name, film.film_pub_year)
                douban_film = db.get_film_detail(douban_id)
                film.stars = douban_film["rating"]["average"]
                film.ratings_count = douban_film["ratings_count"]
                film.reviews_count = douban_film["reviews_count"]
                film.comments_count = douban_film["comments_count"]
                film.wish_count = douban_film["wish_count"]
                film.film_intro = douban_film["summary"]
                film.save()
            else:
                continue
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('获取豆瓣成功\n')