from django.contrib import admin
from core.models import *
# Register your models here.


class Media:
    js = (

        '/static/js/tinymce/tinymce.min.js',
        '/static/js/tinymce/adminconfig.js',

    )
admin.site.register(News)
# admin.site.register(FILM)
# admin.site.register(TVSERIES)
# admin.site.register(TAG_FILM)
