from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# call of public pages
@login_required
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
def dashboard(request):
    return render(request, 'dashboard/index.html')

#call profile page
def profile(request):
    return render(request, 'dashboard/users-profile.html')

#call settings page
def settings(request):
    return render(request, 'dashboard/settings.html')