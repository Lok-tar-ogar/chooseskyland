from django.contrib import admin
from core.models import *
# Register your models here.


class TextFiledAdmin(admin.ModelAdmin):

    class Media:
        js = (

            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/config.js',

        )

admin.site.register(News, TextFiledAdmin)
# admin.site.register(FILM)
# admin.site.register(TVSERIES)
# admin.site.register(TAG_FILM)
