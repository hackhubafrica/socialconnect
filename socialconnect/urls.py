"""
URL configuration for socialconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# socialconnect/urls.py
from django.contrib import admin
from django.urls import path, include
from main import views  # Import views from the main app


urlpatterns = [
    path('', views.home, name='home'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Includes login, logout, signup URLs
    #path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),  
]







