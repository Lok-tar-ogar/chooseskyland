"""ThunderMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^news$', views.news),
url(r'^act$', views.activity),
url(r'^news/(?P<id>\d+).aspx$',views.newsdetail),
url(r'^act/(?P<id>\d+).aspx$',views.activitydetail),
    url(r'^b8ff36b3d794898f43312a0a51a39f27.html$', views.vali),
]
