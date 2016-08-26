from django.contrib import admin

# Register your models here.
from .models import Project, Document

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name_of_project']
    search_fields = ['name_of_project']

    class Meta:
        model=Project


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name_of_document']

    class Meta:
        model=Document


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)