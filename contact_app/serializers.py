from django.core.serializers import serialize, get_serializer_formats
from rest_framework import serializers

from contact_app.models import Users, Contacts


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'phone_number']
