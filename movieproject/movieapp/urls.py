from django.contrib import admin
from django.urls import path, include
app_name='movieapp'

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.det,name='det'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.dele,name='dele')
]