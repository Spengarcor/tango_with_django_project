from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    def __init__(self):
        super().__init__()

    list_display = ('title', 'category', 'url')
    

# Register your models here.

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Page, PageAdmin)

