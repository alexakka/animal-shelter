from django.test import TestCase
from django.urls import reverse
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


class TestViews(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test shelter
        self.shelter = Shelter.objects.create(
            shelter_name='Test Shelter',
            city='Test City',
            address='Test Address',
            phone='1234567890',
            email='test@example.com',
            owner=self.user,
        )

        # Create a test animal
        self.animal = Animal.objects.create(
            shelter=self.shelter,
            animal_name='Test Animal',
            species='Test Species',
            breed='Test Breed',
            age=3,
            description='Test Description',
            image='animal_photos/test.jpg',
            available=True,
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_animal_detail_view(self):
        response = self.client.get(reverse('animal_detail', args=[self.animal.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animal_detail.html')


    def test_create_shelter_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_shelter'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_shelter.html')

    def test_shelter_dashboard_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adminindex.html')

    def test_leave_application_view(self):
        response = self.client.get(reverse('leave_application', args=[self.animal.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'application.html')

    def test_add_animal_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addelem.html')
