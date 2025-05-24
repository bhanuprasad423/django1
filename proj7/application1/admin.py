from django.contrib import admin
from application1.models import Place
from application1.models import Hotels
from application1.models import Waiter

class Place_Admin(admin.ModelAdmin):
    list_display=['name','address']
admin.site.register(Place,Place_Admin)

class Hotel_Admin(admin.ModelAdmin):
    list_display=['place']
admin.site.register(Hotels,Hotel_Admin)

class Waiters_Admin(admin.ModelAdmin):
    list_display=['name','email','number','hotel']
admin.site.register(Waiter,Waiters_Admin)