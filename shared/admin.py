from django.contrib import admin
from .models import Gallery, Contact, Settings

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)