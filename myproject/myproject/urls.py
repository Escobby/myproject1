"""
URL configuration for myproject project.

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
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('readAreas/', views.read_areas, name='read_areas'),
    path('createAreas/', views.create_area, name='create_area'),
    path('updateAreas/<int:area_id>/', views.update_area, name='update_area'),
    path('deleteAreas/<int:area_id>/', views.delete_area, name='delete_area'),

    path('readDepartments/',  views.read_departments, name='read_departments'),
    path('createDepartments/', views.create_department, name='create_department'),
    path('updateDepartments/<int:department_id>/', views.update_department, name='update_department'),
    path('deleteDepartments/<int:department_id>/', views.delete_department, name='delete_department'),

    path('createSubdepartment/', views.create_subdepartment, name='create_subdepartment'),
    path('readSubdepartments/', views.read_subdepartments, name='read_subdepartments'),
    path('updateSubdepartment/<int:subdepartment_id>/', views.update_subdepartment, name='update_subdepartment'),
    path('deleteSubdepartment/<int:subdepartment_id>/', views.delete_subdepartment, name='delete_subdepartment'),

    
path('readMachines/',  views.read_machines, name='read_machines'),
path('createMachines/', views.create_machine, name='create_machine'),
path('updateMachines/<int:machine_id>/', views.update_machine, name='update_machine'),
path('deleteMachines/<int:machine_id>/', views.delete_machine, name='delete_machine'),
]
