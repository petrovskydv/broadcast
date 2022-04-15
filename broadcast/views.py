from rest_framework import viewsets, serializers

from broadcast.models import Client, Mailing


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'mobile_operator_code', 'tag', 'time_zone']


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ['id', 'launch', 'end', 'text', 'mobile_operator_code', 'tag']


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
