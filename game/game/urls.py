"""
URL configuration for game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include  
from player import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar_razas/', views.mostrar_razas),
    path('home/', views.home, name='home'),  # Agrega esta URL para la vista de la página de inicio
    path('register/', views.register, name='register'),  # Agrega esta URL para la vista de registro
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
