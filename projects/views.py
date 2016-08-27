from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import AddProjectForm, AddDocumentForm
from .models import Project, Document

# Create your views here.
def home(request):
    return render(request, 'base.html')

def list_project(request):
    projects = Project.objects.all()
    query = request.GET.get("q")
    if query:
        projects = projects.filter(
            Q(name_of_project__icontains=query)
        ).distinct()
    paginator = Paginator(projects, 2)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        'projects': projects
    }
    return render(request, 'project_list.html', context)

def list_document(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def project_detail(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "project_detail.html", {"project": project})

def add_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponse('<h1>Add new project</h1>')
    else:
        form = AddProjectForm()
    return render(request, 'add_project.html', {'form':form})

def add_document(request):
    if request.method == 'POST':
        form = AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponse('<h1>Add new Document</h1>')
    else:
        form = AddDocumentForm()
    context = {
        'form': form
    }
    return render(request, 'add_document.html', context)


