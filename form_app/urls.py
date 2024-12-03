from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/' ,views.user_login, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index , name='index'),
    path('register/' , views.register , name = 'register'), # default register
    
    ] 