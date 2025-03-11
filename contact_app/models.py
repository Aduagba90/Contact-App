import email

from django.contrib.auth import models
from django.db.models import DecimalField, EmailField, CharField


class Contacts(models.Model):
    phone_number = CharField(max_length=30, null=False, unique=True)
    address = CharField(max_length=50, null=False)


class Users(models.Model):
    name = CharField(max_length=30, null=False)
    email = EmailField(max_length=25, unique=True)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)


