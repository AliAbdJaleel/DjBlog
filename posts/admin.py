from django.contrib import admin

# Register your models here.
from .models import Posts



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','draft']
    list_filter = ['draft']
    search_fields = ['title']
    
    
admin.site.register(Posts,ProductAdmin)