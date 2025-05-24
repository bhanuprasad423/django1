from django.contrib import admin
from application1.models import Student

class student_admin(admin.ModelAdmin):
    list_display=['rollno','name','stu_class','phone_no','address']
admin.site.register(Student,student_admin)

