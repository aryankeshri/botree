from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    name_of_project = models.CharField(verbose_name='Name', max_length=50, blank=False, unique=True)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name_of_project

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


class Document(models.Model):
    name_of_document = models.CharField(verbose_name='Name', max_length=100, blank=False, unique=True)
    file = models.FileField(upload_to='pdf')
    project = models.ManyToManyField(Project)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    def __str__(self):
        return self.name_of_document