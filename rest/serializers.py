from rest_framework import serializers
from .models import Element


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'


class StoichiometrySerializer(serializers.Serializer):
    reactants = serializers.DictField(child=serializers.FloatField())
    products = serializers.DictField(child=serializers.FloatField())


class PHCalculatorSerializer(serializers.Serializer):
    concentration = serializers.FloatField()


class IdealGasLawSerializer(serializers.Serializer):
    pressure = serializers.FloatField()
    volume = serializers.FloatField()
    temperature = serializers.FloatField()
