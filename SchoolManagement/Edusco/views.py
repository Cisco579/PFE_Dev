from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, student_required

@login_required
def index(request):
    return render(request, 'public/index.html')

@login_required
def contact(request):
    return render(request, 'public/contact.html')

@login_required
def trainings(request):
    return render(request, 'public/trainings.html')

@login_required
def about(request):
    return render(request, 'public/about.html')

#END call public pages

#dashboard pages views start here==>

# call of dashboard page
@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')

#call profile page
@login_required
def profile(request):
    return render(request, 'dashboard/users-profile.html')

#call settings page
@login_required
def settings(request):
    return render(request, 'dashboard/settings.html')

@admin_required
def admin_dashboard(request):
    return render(request, 'dashboard/index.html')

@student_required
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')