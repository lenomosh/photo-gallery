from django.db import models


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def save_location(self) -> None:
        self.save()

    def update_location(self, name) -> None:
        self.name = name
        self.save()

    def delete_location(self) -> None:
        self.delete()
