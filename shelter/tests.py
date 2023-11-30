from django.test import TestCase
from django.contrib.auth.models import User
from .models import Shelter, Animal, Application


class ShelterModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.shelter = Shelter.objects.create(
            shelter_name='Test Shelter',
            city='Test City',
            address='Test Address',
            phone='1234567890',
            email='test@example.com',
            owner=self.user
        )

    def test_shelter_str(self):
        self.assertEqual(str(self.shelter), 'Test Shelter')


class AnimalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.shelter = Shelter.objects.create(
            shelter_name='Test Shelter',
            city='Test City',
            address='Test Address',
            phone='1234567890',
            email='test@example.com',
            owner=self.user
        )
        self.animal = Animal.objects.create(
            shelter=self.shelter,
            animal_name='Test Animal',
            species='Dog',
            breed='Labrador',
            age=3,
            description='Test Description',
            image='animal_photos/test.jpg',
            available=True
        )

    def test_animal_str(self):
        self.assertEqual(str(self.animal), 'Test Animal')


class ApplicationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.shelter = Shelter.objects.create(
            shelter_name='Test Shelter',
            city='Test City',
            address='Test Address',
            phone='1234567890',
            email='test@example.com',
            owner=self.user
        )
        self.animal = Animal.objects.create(
            shelter=self.shelter,
            animal_name='Test Animal',
            species='Dog',
            breed='Labrador',
            age=3,
            description='Test Description',
            image='animal_photos/test.jpg',
            available=True
        )
        self.application = Application.objects.create(
            first_name='John',
            second_name='Doe',
            phone='9876543210',
            email='john@example.com',
            status=True,
            animal=self.animal
        )

    def test_application_str(self):
        self.assertEqual(str(self.application), 'John Doe')
