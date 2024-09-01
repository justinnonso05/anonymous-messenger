from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('auth/', views.auth, name="auth"),
    path('', views.user_home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name = 'login'),
    path('login/', auth_views.LogoutView.as_view(template_name = 'auth/login.html'), name = 'logout'),
    path('register/', views.signup, name = 'register'),
    path('send_message/<str:username>', views.send_message, name="send_message")
]
