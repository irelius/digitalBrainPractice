"""
URL configuration for taskTracker project.

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
from django.urls import path

from app import views

urlpatterns = [
    path('', views.main, name="main"),
    path('admin/', admin.site.urls),
    path('api/tasks/get/', views.api_get_tasks, name="api-tasks-get"),
    path('api/tasks/create/', views.api_create_task, name="api-tasks-create"),
    path('api/tasks/delete/<int:task_id>/', views.api_delete_task, name="api-tasks-delete")
]
