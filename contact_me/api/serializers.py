from rest_framework import serializers
from api.models import ContactForm


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactForm
    fields = '__all__'