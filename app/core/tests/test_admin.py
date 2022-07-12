"""
Test for Django admin
"""

from http import client
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSitetests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@email.com',
            password='pass123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@email.com',
            password='pass123',
            name='Test User'
        )

    def test_users_list(self):
        """Test uses are listed on page"""

        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """Test the edit page for user"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test create user page"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)