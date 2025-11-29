from django.contrib import admin
from .models import Elonlar, Yangiliklar, Yunalishlar


@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}

    
@admin.register(Yunalishlar)
class YunalishlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']