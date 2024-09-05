from django.urls import path
from projects.views import *

urlpatterns = [
    path('add_project/', add_project_view, name='add_project'),
    path('all-projects/', all_projects_view, name="all_projects"),
]
