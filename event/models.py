from django.db import models

from authentication.models import User


class Event(models.Model):
    client = models.ForeignKey('Client', related_name='client_of_event', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey('authentication.User', related_name='event_support', on_delete=models.CASCADE)
    event_status = models.ForeignKey('Status', related_name='status_of_event', on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f'Event of {self.event_date}'


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contract(models.Model):
    client = models.ForeignKey('Client', related_name='client_of_contract', on_delete=models.CASCADE)
    sales_contact = models.ForeignKey('authentication.User', related_name='sales_contact_of_contract',
                                      on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return f'Contract {self.id} with {self.client.first_name} {self.client.last_name} as customer'


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey('authentication.User', related_name='contact_of_client', null=True, blank=True,
                                      on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
