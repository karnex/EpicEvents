from django.contrib import admin

from event.models import Event, Status, Contract, Client

admin.site.register(Event)
admin.site.register(Status)
admin.site.register(Contract)
admin.site.register(Client)
