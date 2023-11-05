from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
]
