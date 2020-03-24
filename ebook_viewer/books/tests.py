from django.test import TestCase
from rest_framework.test import APITestCase, URLPatternsTestCase

# Create your tests here.
class APItests(APITestCase, URLPatternsTestCase):
    
    def test_get_all(self):
        response = self.client.get('books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)