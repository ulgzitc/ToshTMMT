from django.contrib import admin
from .models import Elonlar, Yangiliklar, Yunalishlar, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    fields = ('image', 'caption',) 
    extra = 1 



@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryImageInline]


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryImageInline]

    
@admin.register(Yunalishlar)
class YunalishlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']

