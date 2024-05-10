from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'page_url', 'about', 'banner_type')
    search_fields = ('title', 'page_url', 'banner_type')
    list_filter = ('banner_type', 'created_at', 'updated_at')
    ordering = ('-created_at',)

