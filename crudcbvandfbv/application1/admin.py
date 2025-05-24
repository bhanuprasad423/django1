from django.contrib import admin

from application1.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','grade']
admin.site.register(Student,StudentAdmin)

