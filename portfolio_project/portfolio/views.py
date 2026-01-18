from django.shortcuts import render
from .models import Project, Certification

def home(requests):
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'projects': projects,
        'certifications': certifications,
    }
    return render(requests, 'portfolio/home.html', context)