from django.contrib import admin
from .models import Project, Certification

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'technologies')
    ordering = ('-created_at',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_obtained')
    list_filter = ('issuer', 'date_obtained')
    search_fields = ('title', 'issuer', 'description')
    ordering = ('-date_obtained',)