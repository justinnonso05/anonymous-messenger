from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

admin.site.site_title = "Blog site admin (DEV)"
admin.site.site_header = "Admin Panel"
admin.site.index_title = "Site administration"

urlpatterns = [
    path('auth/', views.auth, name="auth"),
    path('', views.user_home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name = 'login'),
    path('login/', auth_views.LogoutView.as_view(template_name = 'auth/login.html'), name = 'logout'),
    path('register/', views.signup, name = 'register'),
    path('send_message/<str:username>', views.send_message, name="send_message")
]
