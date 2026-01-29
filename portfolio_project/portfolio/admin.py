from django.contrib import admin
from .models import ContactMessage, Project, Certification, Skill, Education

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


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    
    def has_add_permission(self, request):
        return False  # Don't allow adding messages from admin
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'order')
    list_editable = ('proficiency', 'order')
    ordering = ('order', 'name')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    list_filter = ('start_date',)
    ordering = ('order', '-start_date')