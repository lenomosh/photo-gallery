from django.test import TestCase
# Create your tests here.
from categories.models import Category
from images.models import Image
from locations.models import Location
from django.core.files.uploadedfile import SimpleUploadedFile



class TestImage(TestCase):

    def setUp(self):
        self.category = Category(name="Test cat")
        self.category.save_category()
        self.location = Location(name="Test Loc")
        self.location.save_location()

        self.image = Image(
            name="Test Img",
            location_id=self.location,
            category_id=self.category,
            image=SimpleUploadedFile(name='image_test.jpg',
                                     content=open('photo_gallery/static/images/default_location.jpg', 'rb').read(),
                                     content_type='image/jpeg')
        )

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_object_instance(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertIsInstance(images[0], Image)

    def test_del_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_updated_image(self):
        self.image.save_image()
        data = dict(name="New Name")
        self.image.update_image(self.image.id,data)
        self.assertTrue(self.image.name, "New Name")

    def test_get_img_by_id(self):
        self.image.save_image()
        print(self.image)
        res = self.image.get_image_by_id(image_id=self.image.id)
        self.assertIsInstance(res,Image)

    def test_filter_img_by_loc(self):
        self.image.save_image()
        res = self.image.filter_by_location(location_id=self.location.id)
        self.assertTrue(len(res),1)
        self.assertEqual(res[0].location_id.name,self.location.name)

    def test_search_image(self):
        self.image.save_image()
        res = self.image.search_image(category_id=self.category.id)
        self.assertTrue(len(res), 1)
        self.assertEqual(res[0].category_id.name, self.category.name)

