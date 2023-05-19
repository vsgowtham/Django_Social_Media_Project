"""social_media_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from media_app import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up' ),
    path('signin/', views.sign_in, name='sign_in'),
    path('signout/', views.sign_out, name='sign_out'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
    path('add_post/', views.add_post, name='add_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('make_admin/<int:user_id>/', views.make_admin, name='make_admin')

]