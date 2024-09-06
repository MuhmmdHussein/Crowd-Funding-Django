from django.urls import path
from projects.views import *

urlpatterns = [
    path('add_project/', add_project_view, name='add_project'),
    path('category/<int:category_id>', category_projects, name="category"),
    path('all-projects/', all_projects_view, name="all_projects"),
    path('project-details/<int:project_id>', project_details_view, name='project_details')
]
