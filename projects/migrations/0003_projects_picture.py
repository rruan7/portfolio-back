# Generated by Django 4.0.2 on 2022-02-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_todo_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='picture',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='images/'),
        ),
    ]
