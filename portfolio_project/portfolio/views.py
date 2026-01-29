from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Certification, Skill, ContactMessage, Education
from .forms import ContactForm

def home(requests):
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    contact_form = ContactForm()
    
    if requests.method == 'POST':
        contact_form = ContactForm(requests.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(requests, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(requests, 'Please correct the errors below.')
    
    context = {
        'projects': projects,
        'certifications': certifications,
        'skills': skills,
        'education': education,
        'contact_form': contact_form,
    }
    return render(requests, 'portfolio/home.html', context)