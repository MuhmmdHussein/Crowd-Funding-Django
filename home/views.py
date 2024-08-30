from django.shortcuts import render
from .models import Project

def homepage(request):
    context = {
        'title': 'Welcome to My Website',
        'message': 'This is a simple homepage.',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'home/homepage.html', context)


from django.shortcuts import render

def all_projects(request):
     projects = Project.objects.all() 
     context = {
        'projects': projects,
    }
     return render(request, 'home/all_projects.html')
