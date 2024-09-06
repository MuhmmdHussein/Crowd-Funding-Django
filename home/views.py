from django.shortcuts import render

from projects.models import Category
from .models import Project

def homepage(request):

    all_categories = Category.objects.all()
    return render(request, 'home/homepage.html', {'all_categories': all_categories})




def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'home/all_projects.html', {'projects': projects})


def home_view(request):
    context = {
      'hero': 'img/hero.png'       
    }
    return render(request, 'home/homepage.html', context)