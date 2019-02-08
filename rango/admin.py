from django.contrib import admin
from rango.models import Category
from rango.models import Page
from rango.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
