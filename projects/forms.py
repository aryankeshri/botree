from django import forms
from .models import Project, Document


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name_of_project']

class AddDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name_of_document', 'project', 'file',]

    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     file_base, type = file.split('.')
    #     if not type == 'pdf':
    #         raise forms.ValidationError('Please use .pdf files only!')
    #     return file
