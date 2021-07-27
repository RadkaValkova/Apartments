from django.db import models

from Apart.inquiry.inquiry_choices import CATEGORY_CHOICES


class CategoryModel(models.Model):
    name = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    def __str__(self):
        return f'{self.name}'


class Inquiry(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    town = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1000)

