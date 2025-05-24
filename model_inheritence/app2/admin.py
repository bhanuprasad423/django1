from django.contrib import admin

from django.contrib import admin
from app2.models import StudentModel,TeacherModel

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','address','roll_no','standard']
admin.site.register(StudentModel,StudentAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_no','address','subject','salary']
admin.site.register(TeacherModel,TeacherAdmin)

