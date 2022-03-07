from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'category', 'app_link', 'source_code', 'picture_link')