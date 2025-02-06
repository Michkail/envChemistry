import math
import re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Element
from .serializers import (ElementSerializer, MolarMassSerializer, ReactantProductSerializer, PHCalculatorSerializer,
                          IdealGasLawSerializer, VanDerWaalsSerializer, EquilibriumSerializer, GibbsSerializer,
                          CellPotentialSerializer, RateLawSerializer, HenryLawSerializer, TitrationSerializer,
                          RaoultLawSerializer, EnthalpySerializer, BufferSerializer, HessLawSerializer,
                          NernstSerializer, FreezingBoilingSerializer, MoleFractionSerializer, HalfLifeSerializer,
                          HeatCapacitySerializer, GasDiffusionSerializer)


class ElementListView(APIView):
    @staticmethod
    def get(request):
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)

        return Response({
            "message": "Success",
            "data": serializer.data
        })


class MolarMassView(APIView):
    @staticmethod
    def post(request):
        serializer = MolarMassSerializer(data=request.data)

        if serializer.is_valid():
            formula = serializer.validated_data['formula']
            elements = {e.symbol: e.atomic_mass for e in Element.objects.all()}
            element_counts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
            total_mass = 0.0

            for element, count in element_counts:
                count = int(count) if count else 1

                if element in elements:
                    total_mass += elements[element] * count

                else:
                    return Response({
                        "message": f"Element {element} not found",
                        "data": None
                    }, status=400)

            return Response({
                "message": "Success",
                "data": {
                    "formula": formula,
                    "molar_mass": total_mass
                }
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoichiometryMoleRatioView(APIView):
    def post(self, request):
        serializer = ReactantProductSerializer(data=request.data)

        if serializer.is_valid():
            reactants = serializer.validated_data['reactants']
            products = serializer.validated_data['products']
            result = self.calculate_stoichiometry(reactants, products)

            return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def calculate_stoichiometry(reactants, products):
        molar_ratio = {
            product: {
                reactant: products[product] / reactants[reactant] for reactant in reactants
            } for product in products
        }

        return {
            "message": "Success",
            "data": {
                "molar_ratio": molar_ratio
            }
        }


class StoichiometryReactantProductView(APIView):
    def post(self, request):
        serializer = ReactantProductSerializer(data=request.data)

        if serializer.is_valid():
            reactants = serializer.validated_data['reactants']
            products = serializer.validated_data['products']

            result = self.determine_reactants_products(reactants, products)

            return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def determine_reactants_products(reactants, products):
        limiting_reactant = min(reactants, key=lambda r: reactants[r] / min(products.values()))

        return {
            "message": "Success",
            "data": {
                "limiting_reactant": limiting_reactant,
                "reactants": reactants,
                "products": products
            }
        }


#  Lomonosov-Lavoisier
class StoichiometryLomonosovLavoisierView(APIView):
    def post(self, request):
        serializer = ReactantProductSerializer(data=request.data)

        if serializer.is_valid():
            reactants = serializer.validated_data['reactants']
            products = serializer.validated_data['products']
            result = self.check_mass_conservation(reactants, products)

            return Response(result, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_mass_conservation(reactants, products):
        total_mass_reactants = sum(reactants.values())
        total_mass_products = sum(products.values())

        is_conserved = abs(total_mass_reactants - total_mass_products) < 1e-6  # little tolerance for floating point

        return {
            "message": "Success" if is_conserved else "Mass is not conserved",
            "data": {
                "total_mass_reactants": total_mass_reactants,
                "total_mass_products": total_mass_products,
                "mass_conserved": is_conserved
            }
        }


class CalcPHView(APIView):
    @staticmethod
    def post(request):
        serializer = PHCalculatorSerializer(data=request.data)

        if serializer.is_valid():
            concentration = serializer.validated_data['concentration']
            ph = -math.log10(concentration)
            poh = 14 - ph

            return Response({
                "message": "Success",
                "data": {
                    "pH": ph, "pOH": poh
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GasLawView(APIView):
    @staticmethod
    def post(request):
        serializer = IdealGasLawSerializer(data=request.data)

        if serializer.is_valid():
            pressure = serializer.validated_data['pressure']
            volume = serializer.validated_data['volume']
            temperature = serializer.validated_data['temperature']
            n = (pressure * volume) / (0.0821 * temperature)

            return Response({
                "message": "Success",
                "data": {
                    "n": n
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VanDerWaalsView(APIView):
    @staticmethod
    def post(request):
        serializer = VanDerWaalsSerializer(data=request.data)

        if serializer.is_valid():
            p = serializer.validated_data['pressure']  # Tekanan (atm)
            v = serializer.validated_data['volume']  # Volume (L)
            n = serializer.validated_data['moles']  # Jumlah mol
            t = serializer.validated_data['temperature']  # Suhu (K)
            a = serializer.validated_data['const_a']  # Konstanta a (L² atm/mol²)
            b = serializer.validated_data['const_b']  # Konstanta b (L/mol)
            r = 0.0821  # Konstanta gas (L atm / mol K)

            # Gas Van der Waals Law: (P + (a * n² / V²)) * (V - n * b) = n * R * T
            p_vdw = ((n * r * t) / (v - n * b)) - (a * n**2 / v**2)

            return Response({
                "message": "Success",
                "data": {
                    "corrected_pressure": p_vdw
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquilibriumConstantView(APIView):
    @staticmethod
    def post(request):
        serializer = EquilibriumSerializer(data=request.data)

        if serializer.is_valid():
            products = serializer.validated_data["products"]  # List of (concentration, coefficient)
            reactants = serializer.validated_data["reactants"]  # List of (concentration, coefficient)
            t = serializer.validated_data["temperature"]  # Suhu dalam Kelvin
            kc = math.prod([c ** co for c, co in products]) / math.prod([c ** co for c, co in reactants])

            return Response({
                "message": "Success",
                "data": {
                    "Kc": kc
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3. Energi Bebas Gibbs
class GibbsFreeEnergyView(APIView):
    @staticmethod
    def post(request):
        serializer = GibbsSerializer(data=request.data)

        if serializer.is_valid():
            delta_h = serializer.validated_data["delta_h"]  # kJ/mol
            delta_s = serializer.validated_data["delta_s"]  # J/(mol K)
            t = request.data.get("temperature")  # K
            delta_g = delta_h - (t * delta_s / 1000)  # ΔG = ΔH - TΔS
            spontaneity = "Spontaneous" if delta_g < 0 else "Non-spontaneous"

            return Response({
                "message": "Success",
                "data": {
                    "Gibbs_free_energy": delta_g,
                    "reaction": spontaneity
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 4. Potensial Sel Galvani
class CellPotentialView(APIView):
    @staticmethod
    def post(request):
        serializer = CellPotentialSerializer(data=request.data)

        if serializer.is_valid():
            e_cathode = serializer.validated_data["e_cathode"]  # Potensial reduksi katoda (V)
            e_anode = serializer.validated_data["e_anode"]  # Potensial reduksi anoda (V)
            e_cell = e_cathode - e_anode  # E° = E°katoda - E°anoda

            return Response({
                "message": "Success",
                "data": {
                    "cell_potential": e_cell
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 5. Laju Reaksi
class RateLawView(APIView):
    @staticmethod
    def post(request):
        serializer = RateLawSerializer(data=request.data)

        if serializer.is_valid():
            k = serializer.validated_data["rate_constant"]  # Konstanta laju
            concentrations = serializer.validated_data["concentrations"]  # List [(conc, order)]
            rate = k * math.prod([c ** o for c, o in concentrations])

            return Response({
                "message": "Success",
                "data": {
                    "reaction_rate": rate
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 6. Hukum Henry
class HenryLawView(APIView):
    @staticmethod
    def post(request):
        serializer = HenryLawSerializer(data=request.data)

        if serializer.is_valid():
            kh = serializer.validated_data["henry_constant"]  # Konstanta Henry
            p_gas = serializer.validated_data["gas_pressure"]  # List [(conc, order)]
            concentration = kh * p_gas

            return Response({
                "message": "Success",
                "data": {
                    "gas_solubility": concentration
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 7. Titik Ekuivalen Titrasi
class TitrationEquivalenceView(APIView):
    @staticmethod
    def post(request):
        serializer = TitrationSerializer(data=request.data)

        if serializer.is_valid():
            m1 = serializer.validated_data["acid_morality"]
            v1 = serializer.validated_data["acid_volume"]
            m2 = serializer.validated_data["base_molarity"]
            v2 = (m1 * v1) / m2  # M1V1 = M2V2

            return Response({
                "message": "Success",
                "data": {
                    "equivalence_volume": v2
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 8. Hukum Raoult
class RaoultLawView(APIView):
    @staticmethod
    def post(request):
        serializer = RaoultLawSerializer(data=request.data)

        if serializer.is_valid():
            p_pure = request.data.get("pure_pressure")  # Tekanan uap zat murni
            x_solute = request.data.get("solute_fraction")  # Fraksi mol zat terlarut
            p_solution = p_pure * (1 - x_solute)

            return Response({
                "message": "Success",
                "data": {
                    "vapor_pressure_solution": p_solution
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 9. Entalpi & Entropi
class EnthalpyEntropyView(APIView):
    def post(self, request):
        serializer = EnthalpySerializer(data=request.data)

        if serializer.is_valid():
            q = serializer.validated_data["heat"]  # Kalor (J)
            t = serializer.validated_data["temperature"]  # Suhu (K)
            entropy = q / t  # S = q / T

            return Response({
                "message": "Success",
                "data": {
                    "entropy_change": entropy
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 10. pH Larutan Buffer
class BufferPHView(APIView):
    @staticmethod
    def post(request):
        serializer = BufferSerializer(data=request.data)

        if serializer.is_valid():
            pka = serializer.validated_data["pka"]
            a_con = serializer.validated_data["acid_concentration"]
            b_con = serializer.validated_data["base_concentration"]
            ph = pka + math.log10(b_con / a_con)

            return Response({
                "message": "Success",
                "data": {
                    "buffer_pH": ph
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HessLawView(APIView):
    @staticmethod
    def post(request):
        serializer = HessLawSerializer(data=request.data)

        if serializer.is_valid():
            """
            Calculating enthalpy change (ΔH) based on Hess' law.
            Input: {"reactants": [ΔH1, ΔH2], "products": [ΔH3, ΔH4]}
            """
            # data = request.POST
            # reactants = sum(map(float, data.getlist("reactants", [])))
            # products = sum(map(float, data.getlist("products", [])))
            reactants = sum(map(float, serializer.validated_data["reactants"]))
            products = sum(map(float, serializer.validated_data["products"]))
            delta_h = products - reactants

            return Response({
                "message": "Success",
                "data": {
                    "delta_h": delta_h
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NernstEquationView(APIView):
    @staticmethod
    def post(request):
        serializer = NernstSerializer(data=request.data)

        if serializer.is_valid():
            """
            Menghitung potensial elektroda dengan persamaan Nernst.
            Input: {"E0": 1.1, "n": 2, "Q": 0.1}
            """
            # data = request.POST
            # eo = float(data.get("E0", 0))
            # n = float(data.get("n", 1))
            # q = float(data.get("Q", 1))
            eo = serializer.validated_data["eo"]
            n = serializer.validated_data["n"]
            q = serializer.validated_data["q"]
            e = eo - (0.0591 / n) * math.log10(q)

            return Response({
                "message": "Success",
                "data": {
                    "E": e
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FreezingBoilingPointView(APIView):
    @staticmethod
    def post(request):
        serializer = FreezingBoilingSerializer(data=request.data)

        if serializer.is_valid():
            # data = request.POST
            # kf = float(data.get("kf", 1.86))
            # kb = float(data.get("kb", 0.51))
            # m = float(data.get("m", 1))
            # i = float(data.get("i", 1))
            kf = serializer.validated_data["kf"]
            kb = serializer.validated_data["kb"]
            m = serializer.validated_data["m"]
            i = serializer.validated_data["i"]
            """
            Calculating freezing point depression and boiling point rise.
            Input: {"kf": 1.86, "kb": 0.51, "m": 2, "i": 1}
            """
            delta_tf = i * kf * m
            delta_tb = i * kb * m

            return Response({
                "message": "Success",
                "data": {
                    "delta_Tf": delta_tf,
                    "delta_Tb": delta_tb
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoleFractionView(APIView):
    @staticmethod
    def post(request):
        serializer = MoleFractionSerializer(data=request.data)

        if serializer.is_valid():
            # data = request.POST
            # nA = float(data.get("nA", 0))
            # nB = float(data.get("nB", 0))
            na = serializer.validated_data["na"]
            nb = serializer.validated_data["nb"]
            """
            Calculating the mole fraction of a solution.
            Input: {"nA": 2, "nB": 3}
            """
            total_moles = na + nb
            xa = na / total_moles if total_moles else 0
            xb = nb / total_moles if total_moles else 0

            return Response({
                "message": "Success",
                "data": {
                    "xA": xa, "xB": xb
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HalfLifeView(APIView):
    @staticmethod
    def post(request):
        serializer = HalfLifeSerializer(data=request.data)

        if serializer.is_valid():
            # data = request.POST
            # k = float(data.get("k", 1))
            k = serializer.validated_data["k"]
            """
            Calculating reaction half-life (1st order).
            Input: {"k": 0.1}
            """
            half_life = 0.693 / k

            return Response({
                "message": "Success",
                "data": {
                    "half_life": half_life
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeatCapacityView(APIView):
    @staticmethod
    def post(request):
        serializer = HeatCapacitySerializer(data=request.data)

        if serializer.is_valid():
            # data = request.POST
            # m = float(data.get("m", 1))
            # c = float(data.get("c", 4.18))
            # delta_T = float(data.get("delta_T", 1))
            m = serializer.validated_data["m"]
            c = serializer.validated_data["c"]
            delta_t = serializer.validated_data["delta_t"]
            """
            Calculating heat based on heat capacity.
            Input: {"m": 2, "c": 4.18, "delta_T": 10}
            """
            q = m * c * delta_t

            return Response({
                "message": "Success",
                "data": {
                    "q": q
                }
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GasDiffusionView(APIView):
    @staticmethod
    def post(request):
        serializer = GasDiffusionSerializer(data=request.data)

        if serializer.is_valid():
            # data = request.POST
            # M1 = float(data.get("M1", 1))
            # M2 = float(data.get("M2", 1))
            # r2 = float(data.get("r2", 1))
            m1 = serializer.validated_data["m1"]
            m2 = serializer.validated_data["m2"]
            r2 = serializer.validated_data["r2"]
            """
            Calculating the gas diffusion rate using Graham's law.
            Input: {"M1": 16, "M2": 32, "r2": 1}
            """
            m1 = serializer
            r1 = r2 * math.sqrt(m2 / m1)

            return Response({
                "message": "Success",
                "data": {
                    "r1": r1
                }
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
