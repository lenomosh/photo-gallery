from django.test import TestCase
from locations.models import Location
# Create your tests here.


class TestLocation(TestCase):

    def setUp(self):
        self.location = Location(name="Test Location")

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_object_instance(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertIsInstance(locations[0], Location)

    def test_del_location(self):
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_updated_location(self):
        self.location.save_location()
        self.location.update_location(name="New Name")
        self.assertTrue(self.location.name, "New Name")