from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddProjectForm, AddDocumentForm
from .models import Project, Document

# Create your views here.
def list_project(request):
    projects_list = Project.objects.all()
    paginator = Paginator(projects_list, 10)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)
    return render(request, 'project_list.html', {'projects': projects})

def list_document(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def project_detail(request, project):
    project = get_object_or_404(Project, slug=project)
    return render(request, "project_detail.html", {"project": project})

def add_project(request):
    form = AddProjectForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponse('<h1>Add new project</h1>')
    context = {
        form: AddProjectForm
    }
    return render(request, 'add_project.html',context)

def add_document(request):
    form = AddDocumentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponse('<h1>Add new Document</h1>')
    context = {
        form: AddDocumentForm
    }
    return render(request, 'add_document.html',context)


