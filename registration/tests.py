from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpViewTests(TestCase):

    def setUp(self):
        # Sample data for testing
        self.signup_url = reverse('signup')
        self.valid_user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        self.invalid_user_data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': 'differentpassword'
        }

    def test_signup_view_renders_correct_template(self):
        # Checking that the sign up view uses the correct template
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

    def test_signup_success(self):
        # Testing a successful registration
        response = self.client.post(self.signup_url, data=self.valid_user_data)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('login')) 
        self.assertTrue(User.objects.filter(username='testuser').exists()) 

    def test_signup_failure_due_to_invalid_data(self):
        # Testing failure due to invalid data
        response = self.client.post(self.signup_url, data=self.invalid_user_data)
        self.assertEqual(response.status_code, 200) 
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")

    def test_duplicate_email_fails(self):
        
        # Create a user with the test email
        User.objects.create_user(username='testuser1', email='test@example.com', password='password123')
        
        # Try to register a user with the same email
        response = self.client.post(reverse('signup'), {
            'username': 'testuser2',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        
        # Check that the form has the expected error
        self.assertFormError(response, 'form', 'email', 'User with this email already exists.')

    def test_invalid_password(self):
        # Test with a password that is too short
        response = self.client.post(reverse('signup'), {
            'username': 'testuser3',
            'email': 'newuser@example.com',
            'password1': 'short',
            'password2': 'short'
        })
        
        # Check that the form has the password length error
        self.assertFormError(response, 'form', 'password2', 'This password is too short. It must contain at least 8 characters.')
