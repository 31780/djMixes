from django.test import TestCase
from django.urls import reverse
from djmixes.models import DJ

class DJListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_djs = 13
        for dj_id in range(number_of_djs):
            DJ.objects.create(name=f'DJ {dj_id}', email=f'dj{dj_id}@example.com', phone='1234567890')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/djmixes/djs/')
        self.assertEqual(response.status_code, 200)

    # Add more tests for other views
