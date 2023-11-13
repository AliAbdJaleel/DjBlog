from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Posts , Category , Comment



class ProductAdmin(SummernoteModelAdmin):
    list_display = ['title','category','draft']
    list_filter = ['draft','category']
    search_fields = ['title']
    summernote_fields = ['content']
    
    
admin.site.register(Posts,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)