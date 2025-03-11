import os

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.sql import UpdateQuery
from django.views.generic import CreateView
from djoser.serializers import UserSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from contact_app.admin import AdminUser
from contact_app.models import Contacts, Users
from contact_app.serializers import UsersSerializer, ContactSerializer


class UserView(RetrieveUpdateDestroyAPIView):
    queryset = AdminUser.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def update_user(self, request, *args, **kwargs):
        queryset = self.get()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateContact(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def add_contacts(self, request):
        queryset = self.get()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)






    # def add_contacts(self):
    #     contact = Contacts()
    #     contact_address = requests.post(contact.address, data=contact.data)
    #     phone = requests.post(contact.phone, data=contact.data)
    #     contact.save()
    #     return contact
    #
    #
    # def delete_contact(self):
    #     contact = Contacts.objects.get(pk=self.kwargs['pk'])
    #     contact.delete()


    # def verify_payments(self):
    #     api = "https://www.google.com/search?q="
    #     headers = os.getenv('API_KEY')
    #     try:
    #         response = requests.get(api, headers=headers)
    #         print(response)
    #     except requests.exceptions.RequestException as exception:
    #         return response.status_code == 404
