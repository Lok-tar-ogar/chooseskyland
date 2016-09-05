# encoding:utf-8
from django.db import models


class NewsImg(models.Model):
    Image = models.FileField('图片（496*360）', upload_to='img/')
    Linkto = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Linkto

    class Meta:
        verbose_name = '首页图片新闻'
        ordering = ['-dimDate']  # sorted news by dimdate


class Carousel(models.Model):
    """docstring for Carousel"""
    Title = models.CharField('标题', max_length=50)
    Image = models.FileField('图片（1920*600）', upload_to='img/')
    Linkto = models.CharField('链接地址（可为空）', max_length=50, blank=True)
    Caption = models.CharField('子标题', max_length=500, blank=True, null=True)
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = '轮播管理'
        ordering = ['-dimDate']  # sorted news by dimdate








class News(models.Model):
    newsTitle = models.CharField('新闻标题', max_length=50)
    newsDetail = models.TextField('新闻详情', max_length=10000)
    # obviously it is what it looks like.
    upLoadImg1 = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg2 = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg3 = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg4 = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    upLoadImg5 = models.FileField(
        '上传新闻中的图片，引用图片请采用"/static/img/xxx.xx"格式', blank=True, null=True, upload_to='img/')
    viewedTimes = models.IntegerField('浏览次数')
    dimDate = models.DateTimeField(auto_now_add=True)  # timezone.now()

    def __str__(self):
        return self.newsTitle

    class Meta:
        verbose_name = '新闻'
        ordering = ['-dimDate']  # sorted news by dimdate





