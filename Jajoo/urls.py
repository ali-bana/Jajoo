"""Jajoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.views.generic import TemplateView
from houses.views import house_create_view, house_edit_view, house_detail_view, house_search_view
from Jajoo import settings


def h(request):
    return render(request, 'signup.html', {})

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('houses/register/', house_create_view),
    path('houses/<int:id>/edit/', house_edit_view),
    path('houses/<int:id>/details/', house_detail_view),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
    path('houses/search/', house_search_view)


]



urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)