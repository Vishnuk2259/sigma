from django.contrib import admin
from .models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)