from django.contrib import admin

# Register your models here.
from .models import Posts , Category , Comment



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','draft']
    list_filter = ['draft','category']
    search_fields = ['title']
    
    
admin.site.register(Posts,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)