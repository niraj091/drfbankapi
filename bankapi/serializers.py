from rest_framework.serializers import ModelSerializer
from bankapi.models import Bank


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

