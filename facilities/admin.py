from django.contrib import admin
from .models import Facilities

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)