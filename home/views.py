from django.shortcuts import render
from .models import Project

def homepage(request):

    return render(request, 'home/homepage.html')




def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'home/all_projects.html', {'projects': projects})


def home_view(request):
    context = {
      'hero': 'img/hero.png'       
    }
    return render(request, 'home/homepage.html', context)