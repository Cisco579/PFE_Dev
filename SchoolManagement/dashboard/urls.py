from django.urls import path
from dashboard import views



urlpatterns = [
    path('dashboard/student', views.index, name='student-dashboard'),
    path('dashboard/profile',views.profile,name='profile'),

]
