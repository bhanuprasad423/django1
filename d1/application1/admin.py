from django.contrib import admin
from application1.models import StudentModel

class StdentAdmin(admin.ModelAdmin):
    list_display=['id','stu_name','roll_no','standard']
admin.site.register(StudentModel,StdentAdmin)
