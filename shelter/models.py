from django.db import models
from django.contrib.auth.models import User


class Shelter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shelter', null=True)
    shelter_name = models.CharField(max_length=55)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner', null=True)

    def __str__(self):
        return self.shelter_name


class Animal(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.PositiveBigIntegerField()
    description = models.TextField(default='')
    image = models.ImageField(upload_to='animal_photos/')
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.animal_name

