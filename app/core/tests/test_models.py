from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test that creation of new user is successful"""
        email = 'test@gamil.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """Test that the email is converted to lowercase on creation"""
        email = 'test@GAMIL.COM'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email_raises_exception(self):
        """Test that creating user with incorrect email value \
        ('' or None) raises correct exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='Testpass123'
            )

    def test_create_new_superuser(self):
        """Test that created superuser has correct attributes"""
        user = get_user_model().objects.create_superuser(
            email='test@gamil.com',
            password='Testpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
