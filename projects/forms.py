from django import forms
from .models import Project, Document


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_of_project',]

class AddDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'project']
