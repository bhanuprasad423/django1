from django.contrib import admin
from application1.models import Product

class product_admin(admin.ModelAdmin):
    list_display=['id','product_id','product_name','price','brand']
admin.site.register(Product,product_admin)