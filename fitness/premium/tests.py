from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class PremiumTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_premium_page(self):
        # Log in the test user
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('premium'))
        self.assertEqual(response.status_code, 200)

    def test_sitemap_page(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<urlset')