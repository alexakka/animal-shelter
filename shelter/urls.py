from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('animal/leave_application/<int:animal_id>/', views.leave_application, name='leave_application'),
    path('shelter/create_shelter/', views.create_shelter, name='create_shelter'),
    path('shelter/dashboard/<int:user_id>', views.shelter_dashboard, name='dashboard'),
    path('shelter/dashboard/add_animal/', views.add_animal, name='add_animal'),

]
