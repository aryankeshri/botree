import os
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Create your models here.

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name_of_project)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def validation_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.pdf']
    if not ext.lower() in valid_extension:
        raise ValidationError(u'Unsupported file extension.')

class Project(models.Model):
    name_of_project = models.CharField(verbose_name="Name", max_length=50, blank=False, unique=True)
    slug = models.SlugField(verbose_name="Slug", unique=True, max_length=50)

    def __str__(self):
        return self.name_of_project

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

class Document(models.Model):
    file = models.FileField(upload_to='pdf', validators=[validation_file_extension], verbose_name='Name of Document')
    project = models.ForeignKey(Project, blank=False, default=False, verbose_name='Name of Project ')
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return '{0}' .format(self.file.name)






