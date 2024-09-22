from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ContactMessages
from .forms import ContactMessagesForm

# Create your tests here.
class ContactFormTests(TestCase):

    def setUp(self):
        # Create an authenticated user for testing
        self.user = User.objects.create_user(username='testuser', email='test123@test.com' ,password='12345')
        self.client.login(username='testuser', password='12345')

    def test_contact_form_valid(self):
        # Test if the form is valid with correct data
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }
        form = ContactMessagesForm(data=form_data)
        self.assertTrue(form.is_valid(), "El formulario debería ser válido con datos correctos")

    def test_contact_form_invalid(self):
        # Test if the form is invalid with missing data
        form_data = {
            'name': '',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }
        form = ContactMessagesForm(data=form_data)
        self.assertFalse(form.is_valid(), "El formulario no debería ser válido si falta el nombre")

    def test_contact_message_creation(self):
        # Test if a contact message is created correctly
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('home'), form_data)
        self.assertEqual(response.status_code, 302, "Debería redirigir después de un envío exitoso")
        self.assertTrue(ContactMessages.objects.filter(name='John Doe').exists(), "Debería crear un mensaje de contacto")

    def test_contact_form_post_with_authenticated_user(self):
        # Test that an authenticated user can submit a form and that it is saved correctly
        form_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Consulta',
            'message': 'Quiero saber más sobre tus servicios'
        }
        response = self.client.post(reverse('home'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessages.objects.count(), 1)

    def test_contact_form_invalid_email(self):
        # Test that the form is not saved if the email is invalid
        form_data = {
            'name': 'John Doe',
            'email': 'not-an-email',
            'subject': 'Test',
            'message': 'Testing invalid email'
        }
        form = ContactMessagesForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
