from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def save_category(self) -> None:
        self.save()

    def update_category(self, name) -> None:
        self.name = name
        self.save()

    def delete_category(self) -> None:
        self.delete()

    def __str__(self):
        return f"{self.name}"
