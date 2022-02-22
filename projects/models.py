from django.db import models

# Create your models here.

def upload_path(instance, filename):
    return '/'.join([str(instance.title), filename])

class Projects(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=60, default="incomplete")
    picture = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def _str_(self):
        return self.title
