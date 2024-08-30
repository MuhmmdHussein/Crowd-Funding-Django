from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Optional: for project image
    link = models.URLField(blank=True, null=True)  # Optional: link to the project

    def __str__(self):
        return self.title
