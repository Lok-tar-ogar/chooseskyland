from django.contrib import admin
from core.models import *
# Register your models here.


class TextFiledAdmin(admin.ModelAdmin):

    class Media:
        js = (

            '/static/js/tinymce/tinymce.min.js',
            '/static/js/tinymce/adminconfig.js',

        )

admin.site.register(News, TextFiledAdmin)
admin.site.register(Activities, TextFiledAdmin)
admin.site.register(NewsImg, TextFiledAdmin)
admin.site.register(serverno, TextFiledAdmin)
admin.site.register(Carousel, TextFiledAdmin)
admin.site.register(Company, TextFiledAdmin)
# admin.site.register(FILM)
# admin.site.register(TVSERIES)
# admin.site.register(TAG_FILM)
