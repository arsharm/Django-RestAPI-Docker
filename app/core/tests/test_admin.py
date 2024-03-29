from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Set up function to perform \\
            set up tasks before any of the \\
            test cases are called in the test class \\

            1.Create a client \\
            2. Create admin user \\
            3.Login admin user \\
            4.Create a user \\
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@airbase.io',
            password='pwd123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='testuser@airbase.io',
            password='pwd123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """
        Test that the user admin page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
