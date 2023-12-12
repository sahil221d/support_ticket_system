from rest_framework import serializers
from .models import User, SupportPerson, Ticket

class SupportPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportPerson
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'