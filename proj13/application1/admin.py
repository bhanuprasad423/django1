from django.contrib import admin
from application1.models import UsersDeatils

class user_details_admin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','username','p1','p2','mobile_no','email']
admin.site.register(UsersDeatils,user_details_admin)



