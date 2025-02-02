from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Element
from .serializers import ElementSerializer, StoichiometrySerializer, PHCalculatorSerializer, IdealGasLawSerializer
import re
import math


class ElementListView(APIView):
    @staticmethod
    def get(request):
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)

        return Response({"message": "Success", "data": serializer.data})


class MolarMassView(APIView):
    @staticmethod
    def post(request):
        formula = request.data.get("formula")

        if not formula:
            return Response({"message": "Formula is required", "data": None}, status=400)

        elements = {e.symbol: e.atomic_mass for e in Element.objects.all()}
        element_counts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
        total_mass = 0.0

        for element, count in element_counts:
            count = int(count) if count else 1

            if element in elements:
                total_mass += elements[element] * count

            else:
                return Response({"message": f"Element {element} not found", "data": None}, status=400)

        return Response({"message": "Success", "data": {"formula": formula, "molar_mass": total_mass}})


class CalcStoichiometryView(APIView):
    def post(self, request):
        serializer = StoichiometrySerializer(data=request.data)

        if serializer.is_valid():
            reactants = serializer.validated_data['reactants']
            products = serializer.validated_data['products']

            # Perhitungan stoikiometri (misal, mencari massa reaktan dan produk)
            # Implementasi dasar stoikiometri, bisa lebih rumit
            result = self.calculate_stoichiometry(reactants, products)

            return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def calculate_stoichiometry(reactants, products):
        molar_ratio = {
            product: {reactant: products[product] / reactants[reactant] for reactant in reactants}
            for product in products
        }

        return {"message": "Success", "data": {"molar_ratio": molar_ratio}}


class CalcPHView(APIView):
    @staticmethod
    def post(request):
        serializer = PHCalculatorSerializer(data=request.data)

        if serializer.is_valid():
            concentration = serializer.validated_data['concentration']

            # Perhitungan pH dari konsentrasi H+
            ph = -math.log10(concentration)
            poh = 14 - ph

            return Response({"message": "Success", "data": {"pH": ph, "pOH": poh}}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GasLawView(APIView):
    @staticmethod
    def post(request):
        serializer = IdealGasLawSerializer(data=request.data)

        if serializer.is_valid():
            pressure = serializer.validated_data['pressure']
            volume = serializer.validated_data['volume']
            temperature = serializer.validated_data['temperature']

            # Perhitungan hukum gas ideal
            n = (pressure * volume) / (0.0821 * temperature)  # Menggunakan konstanta gas ideal 0.0821 L·atm/mol·K
            return Response({"message": "Success", "data": {"n": n}}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
