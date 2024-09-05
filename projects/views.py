from django.shortcuts import render, redirect

from authentication.models import Register
from projects.forms import ProjectForm
from projects.models import Project


# Create your views here.
def all_projects_view(request):
    """
    get all projects record from models
    """

    all_projects = Project.objects.all()
    return render(request, '', {'all_projects': all_projects})


def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():

            project = form.save(commit=False)
            project.created_by = Register.objects.get(id=request.session["user_id"])
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()

    return render(request, 'projects/add_project.html', {'form': form})

