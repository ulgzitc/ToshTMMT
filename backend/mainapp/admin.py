from django.contrib import admin
from .models import Elonlar, Yangiliklar


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