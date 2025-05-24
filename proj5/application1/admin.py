from django.contrib import admin
from application1.models import employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','ename','sal','company')
admin.site.register(employee, EmployeeAdmin)
