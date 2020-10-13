from django.test import TestCase

# Create your tests here.
from categories.models import Category


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category(name="Test Cat")

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_object_instance(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertIsInstance(categories[0], Category)

    def test_del_category(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_updated_category(self):
        self.category.save_category()
        self.category.update_category(name="New Name")
        self.assertTrue(self.category.name,"New Name")
