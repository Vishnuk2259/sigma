from django.contrib import admin
from .models import Partners

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)