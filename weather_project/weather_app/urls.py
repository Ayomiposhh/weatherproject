from django.urls import path, include 
from weather_app import views
from django.contrib.auth import views as auth_views

# from second_project import second_app


app_name = 'weather_app'


urlpatterns = [

    path('home/', views.home, name='home'),

]


