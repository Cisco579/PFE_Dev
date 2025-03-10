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

#dashboard pages views start here==>

# call of dashboard page
# @login_required
# def dashboard(request):
#     return render(request, 'dashboard/index.html')

# #call profile page
# @login_required
# def profile(request):
#     return render(request, 'dashboard/users-profile.html')

# #call settings page
# @login_required
# def settings(request):
#     return render(request, 'dashboard/settings.html')

# @admin_required
# def admin_dashboard(request):
#     return render(request, 'dashboard/index.html')

# @student_required
# def student_dashboard(request):
#     return render(request, 'dashboard/student_dashboard.html')

# @teacher_required
# def teacher_dashboard(request):
#     return render(request,'dashboard/teacher_dashboard')