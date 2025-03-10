from django.contrib import admin
from django.urls import path,include
from Edusco import views

urlpatterns = [
    #django-allauth urls
    path('admin/', admin.site.urls),
    
    #admin urls
    path('accounts/', include('allauth.urls')), 
    
    #include dashboard urls
    path('', include('dashboard.urls')),
    
    #public pages urls
    path('', views.index,name='home'),
    path('contact/', views.contact, name='contact'),
    path('trainings/', views.trainings, name='trainings'),
    path('about/', views.about, name='about'),
    #end of public pages urls
    
  
   

]
