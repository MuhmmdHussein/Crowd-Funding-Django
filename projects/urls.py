from django.urls import path
from projects.views import *

urlpatterns = [
    path('add-project/', add_project_view, name='add-project'),
    path('category/<int:category_id>', category_projects, name="category"),
    path('all-projects/', all_projects_view, name="all_projects"),
    path('project-details/<int:project_id>', project_details_view, name='project_details'),
    path('donate/<int:project_id>', donate, name='donate'),
    path('make_project_comment/<int:project_id>', make_project_comment, name='make_project_comment'),
    path('rate_project/<int:project_id>', rate_project_method, name='rate_project'),
    path('create_tag_method/', create_tage_method, name='create_tag'),
]
