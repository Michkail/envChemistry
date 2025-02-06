from rest_framework import serializers
from .models import Element


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'


class MolarMassSerializer(serializers.Serializer):
    formula = serializers.CharField()


class ReactantProductSerializer(serializers.Serializer):
    reactants = serializers.DictField(child=serializers.FloatField())
    products = serializers.DictField(child=serializers.FloatField())


class PHCalculatorSerializer(serializers.Serializer):
    concentration = serializers.FloatField()


class IdealGasLawSerializer(serializers.Serializer):
    pressure = serializers.FloatField()
    volume = serializers.FloatField()
    temperature = serializers.FloatField()


class VanDerWaalsSerializer(serializers.Serializer):
    pressure = serializers.FloatField()
    volume = serializers.FloatField()
    moles = serializers.FloatField()
    temperature = serializers.FloatField()
    const_a = serializers.FloatField()
    const_b = serializers.FloatField()


class EquilibriumSerializer(serializers.Serializer):
    products = serializers.DictField(child=serializers.FloatField())
    reactants = serializers.DictField(child=serializers.FloatField())
    temperature = serializers.FloatField()


class GibbsSerializer(serializers.Serializer):
    delta_h = serializers.FloatField()
    delta_s = serializers.FloatField()
    temperature = serializers.FloatField()


class CellPotentialSerializer(serializers.Serializer):
    e_cathode = serializers.FloatField()
    e_anode = serializers.FloatField()


class RateLawSerializer(serializers.Serializer):
    rate_constant = serializers.FloatField()
    concentrations = serializers.FloatField()


class HenryLawSerializer(serializers.Serializer):
    henry_constant = serializers.FloatField()
    gas_pressure = serializers.FloatField()


class TitrationSerializer(serializers.Serializer):
    m1 = serializers.FloatField()
    m2 = serializers.FloatField()
    v1 = serializers.FloatField()


class RaoultLawSerializer(serializers.Serializer):
    pure_pressure = serializers.FloatField()
    x_solute = serializers.FloatField()


class EnthalpySerializer(serializers.Serializer):
    heat = serializers.FloatField()
    temperature = serializers.FloatField()


class BufferSerializer(serializers.Serializer):
    pka = serializers.FloatField()
    a_concentration = serializers.FloatField()
    b_concentration = serializers.FloatField()


class HessLawSerializer(serializers.Serializer):
    reactants = serializers.DictField()
    products = serializers.DictField()


class NernstSerializer(serializers.Serializer):
    eo = serializers.FloatField()
    n = serializers.FloatField()
    q = serializers.FloatField()


class FreezingBoilingSerializer(serializers.Serializer):
    kf = serializers.FloatField()
    kb = serializers.FloatField()
    m = serializers.FloatField()
    i = serializers.FloatField()


class MoleFractionSerializer(serializers.Serializer):
    na = serializers.FloatField()
    nb = serializers.FloatField()


class HalfLifeSerializer(serializers.Serializer):
    k = serializers.FloatField()


class HeatCapacitySerializer(serializers.Serializer):
    m = serializers.FloatField()
    c = serializers.FloatField()
    delta_t = serializers.FloatField()


class GasDiffusionSerializer(serializers.Serializer):
    m1 = serializers.FloatField()
    m2 = serializers.FloatField()
    r2 = serializers.FloatField()
