from django.contrib import admin

# Register your models here.
from .models import Project, Document

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name_of_project', 'slug']
    search_fields = ['name_of_project']
    list_filter = ['name_of_project']
    prepopulated_fields = {'slug': ('name_of_project',)}

    class Meta:
        model = Project


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['file', 'created', 'modified']
    search_fields = ['file',]

    class Meta:
        model = Document


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)