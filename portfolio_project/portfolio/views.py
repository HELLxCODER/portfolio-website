from django.shortcuts import render
from .models import Project

def home(requests):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(requests, 'portfolio/home.html', context)