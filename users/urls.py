from django.urls import path, include

from . import views


urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
