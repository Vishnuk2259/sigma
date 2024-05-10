from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_category', 'member_designation')
    search_fields = ('name', 'member_category', 'member_designation')
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)
