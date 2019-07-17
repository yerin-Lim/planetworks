from rest_framework.serializers import ModelSerializer
from .models import Message
from rest_framework.fields import ReadOnlyField

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content','date']