from __future__ import annotations
from django.db import models

# Create your models here.
from typing import List, Dict

from categories.models import Category
from locations.models import Location
import datetime


class CommonFields:
    CREATED_AT = models.DateTimeField(default=datetime.datetime.now)
    UPDATED_AT = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True


class Image(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location_id = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    CREATED_AT = models.DateTimeField(default=datetime.datetime.now)
    UPDATED_AT = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> None:
        return self.name

    def save_image(self) -> None:
        self.save()

    def update_image(self, id: int, data: Dict) -> None:
        Image.objects.filter(id=id).update(**data)

    def delete_image(self) -> None:
        self.delete()

    def get_image_by_id(self, image_id: int) -> Image:
        # import pdb;pdb.set_trace()
        return Image.objects.get(id=image_id)

    def filter_by_location(self, location_id: int) -> List[Image]:
        return Image.objects.filter(location_id=location_id).all()

    def search_image(self, category_id: int) -> List[Image]:
        return Image.objects.filter(category_id=category_id).all()
