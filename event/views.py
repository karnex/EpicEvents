from rest_framework.viewsets import ModelViewSet

from event.models import Client, Contract
from event.serializers import AllDataClientSerializer, LittleDataClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        return AllDataClientSerializer if 'pk' in self.kwargs else LittleDataClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
