
from django.contrib import admin
from application1.models import movies,web_series

class movie_admin(admin.ModelAdmin):
    list_display=['movie_name','movie_frame','budget','hero','director','description','rating']
    list_filter=['hero']
    list_display_links=['movie_name']
    list_editable=['director']
    search_fields=['hero','director']
    ordering=['rating']
    # list_max_show_all=['rating']

admin.site.register(movies, movie_admin) 

class web_admin(admin.ModelAdmin):
    list_display=['series_name','photo','budget','hero','director','description','rating']
admin.site.register(web_series, web_admin)  
