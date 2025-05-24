from django.contrib import admin
from application1.models import Mobiles
# Register your models here.
class Mobile_Admin(admin.ModelAdmin):
    list_display=['img','name','price','delivery']
admin.site.register(Mobiles,Mobile_Admin)