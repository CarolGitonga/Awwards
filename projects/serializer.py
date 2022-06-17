from rest_framework import serializers
from .models import Profile, Project
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'profile_image', 'bio', 'location', 'contact']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'url', 'description', 'image', 'date', 'user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [ 'url', 'username', 'profile', 'projects']