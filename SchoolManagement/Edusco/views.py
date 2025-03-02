from django.shortcuts import render

#home pages views start here==>

# call of home page
def index(request):
    return render(request, 'public/index.html')


#call users profile page


#home pages views end here<===

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