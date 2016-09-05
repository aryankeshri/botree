from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProfileForm
from .models import Profile

def add_profile(request):
    # if not request.user.groups.filter(name='admin') or not request.user.is_superuser:
    # 	raise Http404
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('list_project')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, "add_profile.html", context)
