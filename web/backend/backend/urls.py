"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ds_project.urls.import_data')),
    path('', include('ds_project.urls.student')),
    path('', include('ds_project.urls.faculty')),
    path('', include('ds_project.urls.major')),
    path('', include('ds_project.urls.training_system')),
    path('', include('ds_project.urls.course')),
    path('', include('ds_project.urls.course_type')),
    path('', include('ds_project.urls.group_course_type')),

]
