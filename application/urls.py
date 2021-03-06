"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from application import views

app_name = 'application'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('apply/', views.apply, name='apply'),
    path('account/', views.profile, name='profile'),
    path('account/edit/', views.edit_profile, name='edit_profile'),
    path('account/edit/image/', views.upload_image, name='upload_image'),
    path('users/<int:pk>/', views.user_detail, name='user'),
    path('users/', views.user_list, name='users'),
    path('users/<int:pk>/approve/', views.approve, name='approve'),
    path('users/<int:pk>/disapprove/', views.disapprove, name='disapprove'),
]
