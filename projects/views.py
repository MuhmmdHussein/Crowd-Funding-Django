from django.shortcuts import render, redirect

from authentication.models import Register
from projects.forms import ProjectForm, ProjectImageForm
from projects.models import Project, Category, ProjectImage, Tag


# Create your views here.
def all_projects_view(request):
    """
    get all projects record from models
    """

    all_projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'projects/all_projects.html', {'all_projects': all_projects, 'all_categories': categories})


def category_projects(request, category_id):

    all_projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'projects/all_projects.html', {'all_projects': all_projects, 'all_categories': categories})


def project_details_view(request, project_id):
    project = Project.objects.get(id=project_id)
    project_images = ProjectImage.objects.filter(project_id=project.id)
    tags = project.tags.all()
    print(project.tags)
    counter = []
    counter_index = 1
    for image in project_images:
        counter.append(f'{counter_index}')
        counter_index += 1
    counter.pop()
    return render(request, 'projects/project_details.html', {
        'project': project,
        'project_images': project_images,
        'counter': counter,
        'tags': tags
    })


def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, files=request.FILES)
        images_form = ProjectImageForm(request.POST, files=request.FILES)
        print(form.data)

        if form.is_valid():
            print(form.cleaned_data)
            project = form.save(commit=False)
            project.created_by = Register.objects.get(id=request.session["user_id"])
            project.pictures = form.cleaned_data['pictures']

            project.save()
            tag_ids = request.POST.getlist('tags')  # Assuming 'tags' is the name of the select field in the form
            tags = Tag.objects.filter(id__in=tag_ids)
            project.tags.set(tags)
            images = request.FILES.getlist('images')
            for image in images:
                ProjectImage.objects.create(project=project, image=image)

            return redirect('/')
    else:
        form = ProjectForm()
        images_form = ProjectImageForm()

    return render(request, 'projects/add_project.html', {'form': form, 'image_form': images_form})

