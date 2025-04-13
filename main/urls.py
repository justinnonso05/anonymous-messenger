from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.contrib.auth import logout

admin.site.site_title = "Site Admin"
admin.site.site_url = "/"
admin.site.site_header = "Admin Panel"
admin.site.index_title = "Site administration"

def custom_logout_view(request):
    logout(request)
    return redirect('auth') 

urlpatterns = [
    path('auth/', views.auth, name="auth"),
    path('', views.user_home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name = 'login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', views.signup, name = 'register'),
    path('send_message/<str:username>', views.send_message, name="send_message"),
    path('message/<int:message_id>/', views.message_detail, name="message_detail"),
]
