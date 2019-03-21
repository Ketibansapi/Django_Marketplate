from django.urls import path

from . import views

# Pattern for routes from accounts
urlpatterns = [
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('dashboard', views.dashboard, name = 'dashboard'),
]
