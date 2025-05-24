from django.contrib import admin 
from application1.models import Reporters 
from application1.models import Atricle 
class Reporters_Admin(admin.ModelAdmin):
    list_display=['First_Name','Last_Name','Username','P1','P2','Mobile_Number','Email'] 
admin.site.register(Reporters,Reporters_Admin) 

class Atricle_Admin(admin.ModelAdmin):
    list_display=['headline','public_date','reporter']
admin.site.register(Atricle,Atricle_Admin)

