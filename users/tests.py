from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view(self):
        # Access the register view
        response = self.client.get(reverse('register'))

        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is being used
        self.assertTemplateUsed(response, 'registration/register.html')

        # Test registration with valid data
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })

        # Ensure the response is a redirect after successful registration
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('create_shelter'))

        # Ensure a new user is created in the database
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)

    def test_user_login_view(self):
        # Create a test user for login
        test_user = User.objects.create_user(username='testuser', password='testpassword')

        # Access the user_login view with GET method
        response = self.client.get(reverse('user_login'))

        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is being used
        self.assertTemplateUsed(response, 'registration/login.html')

        # Test login with valid credentials
        response = self.client.post(reverse('user_login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })

        # Ensure the response is a redirect after successful login
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Test login with invalid credentials
        response = self.client.post(reverse('user_login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })

        # Ensure the response status is 200 OK after unsuccessful login
        self.assertEqual(response.status_code, 200)
