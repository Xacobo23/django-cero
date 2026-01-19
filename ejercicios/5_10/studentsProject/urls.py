from django.urls import path
from studentsProjectApp import views

"""Borramos todo lo de admin y añadimos lo siguiente, para camibar la landing page"""
urlpatterns = [
path('', views.home, name='home'),
path('studentForm/', views.StudentCreate.as_view(), name='studentForm'),
path('studentList/', views.StudentList.as_view(), name='studentList'),
path('student/<int:pk>/', views.StudentDetail.as_view(), name='studentDetail')
]