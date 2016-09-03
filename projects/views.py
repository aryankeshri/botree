from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.urlresolvers import reverse

from .forms import AddProjectForm, AddDocumentForm
from .models import Project, Document

# Create your views here.
# listing of projects
def list_project(request, id=None):
    pid = Project.objects.all().filter(pk=id)
    print(pid)
    no_document = len(Document.objects.filter(project__id = pid))
    print(no_document)
    projects = Project.objects.all()
    query = request.GET.get("q")
    if query:
        projects = projects.filter(
            Q(name_of_project__icontains=query)
        ).distinct()
    paginator = Paginator(projects, 10)
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
        'projects': projects,
        'no_document': no_document
    }
    return render(request, 'project_list.html', context)


# listing of documents
def list_document(request):
    documents = Document.objects.all().select_related('project')
    print(documents)
    context = {
        'documents': documents
    }
    return render(request, 'document_list.html', context)


# detail of related project
def project_detail(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    pid = Project.objects.all().filter(name_of_project__icontains=project)
    documents = Document.objects.filter(project__id=pid)
    no_document = len(documents)

    context = {
        "project": project,
        "documents": documents,
        "no_document": no_document
    }
    return render(request, "project_detail.html", context)


# add project
def add_project(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return redirect('list_project')
    else:
        form = AddProjectForm()
    return render(request, 'add_project.html', {'form':form})


# add document
def add_document(request):
    if request.method == 'POST':
        form = AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('list_document')
    else:
        form = AddDocumentForm()

    context = {
        'form': form
    }
    return render(request, 'add_document.html', context)


# delete document from the project
def delete_document(request, id):
    u = get_object_or_404(Document, pk=id).delete()
    print(u)
    return HttpResponseRedirect('/')
