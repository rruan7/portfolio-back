from django.db import models

# Create your models here.

def upload_path(instance, filename):
    return '/'.join([str(instance.title), filename])


class Projects(models.Model):
    CATEGORIES = (
        ('applications', 'Applications'),
        ('miniprojects', 'Mini-Projects'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=60, choices=CATEGORIES, default="applications")
    app_link = models.URLField(default="https://www.reneeruan.com")
    source_code = models.URLField(default="https://github.com/rruan7?tab=repositories")
    picture_link = models.URLField(default="https://user-images.githubusercontent.com/71851361/155896993-a3549ad7-fa6a-4822-baf5-dc9322a5997a.PNG")

    def _str_(self):
        return self.title
