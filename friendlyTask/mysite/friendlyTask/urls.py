from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('photos', views.getData, name='getData'),
    path('add', views.addPhoto, name='addPhoto'),
    path('update/<int:id>', views.updatePhoto, name='updatePhoto'),
    path('delete/<int:id>', views.deletePhoto, name='deletePhoto'),
    path('file/add', views.addPhotoFromFile, name='addPhotoFromFile')
]
