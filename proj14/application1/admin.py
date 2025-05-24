from django.contrib import admin
from application1.models import Login
class login_admin(admin.ModelAdmin):
    list_display=['id','username','password']
admin.site.register(Login,login_admin)

