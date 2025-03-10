from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from dashboard.decorators import admin_required, student_required

# from django.template import loader
# from django.urls import reverse


@login_required
@student_required
def index(request):
    return render(request,'home/index.html')

@login_required
@student_required
def profile(request):
    return render(request,'home/profile')




