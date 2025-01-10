from rest_framework import serializers
from .models import *

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        many = True
        fields = '__all__'