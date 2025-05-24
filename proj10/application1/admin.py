from django.contrib import admin
from application1.models import Products
from application1.models import Customer

class Product_Admin(admin.ModelAdmin):
    list_display=['Pid','Pname','Price','Company','M_date','Exp_date']
admin.site.register(Products,Product_Admin)

class Customer_Admin(admin.ModelAdmin):
    list_display=['Cid','Cname','Address','Mobile_Number','Email_Address']
admin.site.register(Customer,Customer_Admin)