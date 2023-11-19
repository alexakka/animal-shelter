from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('shelter/create_shelter/', views.create_shelter, name='create_shelter'),
    path('shelter/dashboard/<int:user_id>', views.shelter_dashboard, name='shelter_dashboard'),

]
