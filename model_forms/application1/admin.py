from django.contrib import admin
from application1.models import Student

class Student_admin(admin.ModelAdmin):
    list_display=['id','stu_name','roll_no','std','address','marks','nick_name','phone_no']
    list_editable=['phone_no']
    list_filter=['stu_name']
    search_fields=['stu_name','roll_no']
admin.site.register(Student,Student_admin)