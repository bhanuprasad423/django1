from django.contrib import admin
from app3.models import DetailsModel, StudentModel


class DetailAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','address']

admin.site.register(DetailsModel,DetailAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','address','roll_no','standard']
admin.site.register(StudentModel,StudentAdmin)