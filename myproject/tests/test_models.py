from django.test import TestCase
from djmixes.models import DJ, Mix, Profile, Tag

class DJModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DJ.objects.create(name='DJ Test', email='djtest@example.com', phone='1234567890')

    def test_name_label(self):
        dj = DJ.objects.get(id=1)
        field_label = dj._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # Add more tests for other fields and models
