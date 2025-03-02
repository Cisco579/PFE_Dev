
from django.contrib import admin
from django.urls import path,include
from Edusco import views

urlpatterns = [
    path('', views.index,name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile/',views.profile, name='profile'),
    path('dashboard/settings/',views.settings, name='settings'),
    path('admin/', admin.site.urls),

]
