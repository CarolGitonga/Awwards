from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Project(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    image = ImageField(manual_crop='1280x720')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return f'{self.title}'

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

class Rating(models.Model):
  

    design = models.IntegerField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    usability = models.IntegerField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    content = models.IntegerField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    score = models.FloatField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    design_average = models.FloatField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    usability_average = models.FloatField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    content_average = models.FloatField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project} Rating'

