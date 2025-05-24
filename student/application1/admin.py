from django.contrib import admin
from application1.models import StudentsModel,Login

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sname','roll_no','phone_no','standard','sub1','sub2','sub3','sub4','sub5','total_marks','percentage']
    list_filter=['sname']
    search_fields=['sname','roll_no']
admin.site.register(StudentsModel,StudentAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(Login,LoginAdmin)