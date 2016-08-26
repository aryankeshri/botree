from django.db import models

# Create your models here.
class Project(models.Model):
    name_of_project = models.CharField(verbose_name='Name', max_length=50, blank=False)

    def __str__(self):
        return self.name_of_project

class Document(models.Model):
    name_of_document = models.CharField(verbose_name='Name of Document', max_length=100, blank=False)
    file = models.FileField(upload_to='pdf')
    project = models.ManyToManyField(Project)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    def __str__(self):
        return self.name_of_document