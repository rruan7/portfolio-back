from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'picture')

# Register your models here.

admin.site.register(Projects, ProjectsAdmin)
