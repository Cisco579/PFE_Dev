from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .decorators import admin_required, student_required,teacher_required


def index(request):
    return render(request, 'public/index.html')


def contact(request):
    return render(request, 'public/contact.html')


def trainings(request):
    return render(request, 'public/trainings.html')


def about(request):
    return render(request, 'public/about.html')

#END call public pages

