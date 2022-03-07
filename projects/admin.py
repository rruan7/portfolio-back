from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'app_link', 'source_code', 'picture_link')

# Register your models here.

admin.site.register(Projects, ProjectsAdmin)
