# Generated by Django 4.0.5 on 2022-06-16 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_rename_prject_rating_project_project_technologies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='rate',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=155),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
