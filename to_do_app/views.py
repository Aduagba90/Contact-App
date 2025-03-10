import requests
from django.views.generic import CreateView

from to_do_app.models import Contacts


class CreateUserView(CreateView):

    def add_contacts(self):
        contact = Contacts()
        contact_address = requests.post(contact.address, data=contact.data)
        phone = requests.post(contact.phone, data=contact.data)
        contact.save()
        return contact


    def delete_contact(self):
        contact = Contacts.objects.get(pk=self.kwargs['pk'])
        contact.delete()
