from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DecimalField, ForeignKey

from to_do_app.models import Users


class AdminUser(AbstractUser):
    username = CharField(max_length=20, unique=True)
    password = CharField(max_length=20, unique=True, null=False)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


