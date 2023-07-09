from django.test import SimpleTestCase
from django.urls import reverse, resolve
from djmixes.views import dj_list

class TestUrls(SimpleTestCase):
    def test_dj_list_url_is_resolved(self):
        url = reverse('djs')
        self.assertEqual(resolve(url).func, dj_list)

    # Add more tests for other urls
