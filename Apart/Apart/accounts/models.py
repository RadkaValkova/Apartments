from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from Apart.accounts.manager import ApartUserManager


class ApartUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = ApartUserManager()


class Profile(models.Model):
    # profile_image = models.ImageField(
    #     upload_to='profiles',
    #     blank=True,
    # )
    image_url = models.URLField(
        blank=True,
    )

    user = models.OneToOneField(
        ApartUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *

