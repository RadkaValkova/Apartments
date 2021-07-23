from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

from Apart.apart_app.apart_choices import STATUS_CHOICES, CONSTRUCTION_CHOICES, FURNISHING_CHOICES, TOWN_CHOICES, \
    TYPE_CHOICES, DEAL_CHOICES, FINISHING_CHOICES


class TownModel(models.Model):
    name = models.CharField(max_length=20, choices=TOWN_CHOICES, )

    def __str__(self):
        return f'{self.name}'


class TypeModel(models.Model):
    name = models.CharField(max_length=20, choices=TYPE_CHOICES, )

    def __str__(self):
        return f'{self.name}'


class DealModel(models.Model):
    name = models.CharField(max_length=20, choices=DEAL_CHOICES)

    def __str__(self):
        return f'{self.name}'


class StatusModel(models.Model):
    name = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.name}'


class ConstructionModel(models.Model):
    name = models.CharField(max_length=20, choices=CONSTRUCTION_CHOICES)

    def __str__(self):
        return f'{self.name}'


class FurnishingModel(models.Model):
    name = models.CharField(max_length=20, choices=FURNISHING_CHOICES)

    def __str__(self):
        return f'{self.name}'


class FinishingWorksModel(models.Model):
    name = models.CharField(max_length=20, choices=FINISHING_CHOICES)

    def __str__(self):
        return f'{self.name}'


class ApartmentModel(models.Model):
    type = models.ForeignKey(
        TypeModel,
        on_delete=models.SET_NULL,
        null=True
    )
    town = models.CharField(
        max_length=30,
    )
    construction = models.ForeignKey(
        ConstructionModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    construction_year = models.CharField(
        max_length=4,
        blank=True,
    )
    deal = models.ForeignKey(
        DealModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.ForeignKey(
        StatusModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    price_offer = models.PositiveIntegerField()

    price_realized = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0
    )

    pure_area = models.PositiveIntegerField()

    total_area = models.PositiveIntegerField()

    finishing_works = models.ForeignKey(
        FinishingWorksModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    furnishing = models.ForeignKey(
        FurnishingModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    description = models.TextField(
        max_length=1000,
    )
    image = models.ImageField(
        upload_to='aparts',
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )  # blank=False

    email = models.EmailField()

    contact_phone = models.IntegerField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

