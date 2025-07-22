import graphene
import math
from rest.models import Element, Compound, Isotope
from .elements import IsotopeType, ElementListResponse, ElementType, CompoundListResponse, CompoundType
from .inputs import *

    
class UpdateElements(graphene.Mutation):
    class Arguments:
        inputs = graphene.List(ElementUpdateInput, required=True)

    ok = graphene.Boolean()
    messages = graphene.List(graphene.String)

    @staticmethod
    def mutate(root, info, inputs):
        messages = []

        for inp in inputs:
            try:
                el = Element.objects.get(atomic_number=inp.atomic_number)

                for field in ElementUpdateInput._meta.fields:
                    if field != "isotopes":
                        val = getattr(inp, field, None)

                        if val is not None:
                            setattr(el, field, val)

                el.save()

                if inp.isotopes is not None:
                    el.isotopes.all().delete()
                    Isotope.objects.bulk_create([Isotope(element=el,
                                                         symbol=iso.symbol,
                                                         mass=iso.mass,
                                                         abundance=iso.abundance,
                                                         half_life=iso.half_life,
                                                         decay_mode=iso.decay_mode) for iso in inp.isotopes ])

                messages.append(f"Updated atomic_number={inp.atomic_number}")

            except Element.DoesNotExist:
                messages.append(f"Element {inp.atomic_number} not found")

            except Exception as e:
                messages.append(f"Error {inp.atomic_number}: {e}")

        ok = all("Updated" in m for m in messages)

        return UpdateElements(ok=ok, messages=messages)

        

class Mutation(graphene.ObjectType):
    update_element = UpdateElements.Field()


class Query(graphene.ObjectType):
    hello = graphene.String()
    elements = graphene.Field(ElementListResponse)
    compounds = graphene.Field(CompoundListResponse)
    calculate_ph = graphene.Float(input=PHInput(required=True))
    calculate_gibbs = graphene.Float(input=GibbsInput(required=True))

    def resolve_hello(root, info):
        return "Welcome human"

    def resolve_elements(root, info):
        data = [ElementType(atomic_number=el.atomic_number,
                            atomic_mass=el.atomic_mass,
                            atomic_radius=el.atomic_radius,
                            covalent_radius=el.covalent_radius,
                            van_der_waals_radius=el.van_der_waals_radius,
                            symbol=el.symbol,
                            name=el.name,
                            category=el.category,
                            period=el.period,
                            group=el.group,
                            block=el.block,
                            phase=el.phase,
                            density=el.density,
                            melting_point=el.melting_point,
                            boiling_point=el.boiling_point,
                            electron_configuration=el.electron_configuration,
                            electronegativity=el.electronegativity,
                            electron_affinity=el.electron_affinity,
                            electrical_conductivity=el.electrical_conductivity,
                            thermal_conductivity=el.thermal_conductivity,
                            ionization_energy=el.ionization_energy,
                            isotopes=[IsotopeType(symbol=iso.symbol,
                                                  mass=iso.mass) for iso in el.isotopes.all()],
                            oxidation_state=el.oxidation_state,
                            abundance_earth_crust=el.abundance_earth_crust,
                            abundance_universe=el.abundance_universe,
                            specific_heat=el.specific_heat,
                            appearance=el.appearance,
                            crystal_structure=el.crystal_structure,
                            discovery_year=el.discovery_year,
                            discovery_by=el.discovery_by) for el in Element.objects.all()]
        
        return ElementListResponse(message="Success", data=data)

    def resolve_compounds(root, info):
        data = [CompoundType(name=co.name,
                             chemical_formula=co.chemical_formula,
                             category=co.category,
                             bond_type=co.bond_type,
                             properties=co.properties,
                             uses=co.uses,
                             status=co.status,
                             discovery_date=co.discovery_date,
                             discovery_period=co.discovery_period,
                             discovery_by=co.discovery_by,
                             source=co.source) for co in Compound.objects.all()]
        
        return CompoundListResponse(message="Success", data=data)

    def resolve_calculate_ph(root, info, input):
        if input.concentration is None or input.concentration <= 0:
            return None
        return -math.log10(input.concentration)

    def resolve_calculate_gibbs(root, info, input):
        return input.delta_h - input.temperature * input.delta_s

    calculate_cell_potential = graphene.Float(input=CellPotentialInput(required=True))
    def resolve_calculate_cell_potential(root, info, input):
        return input.e_cathode - input.e_anode

    calculate_mole_fraction = graphene.Float(input=MoleFractionInput(required=True))
    def resolve_calculate_mole_fraction(root, info, input):
        return input.na / (input.na + input.nb) if input.na + input.nb != 0 else None

    calculate_half_life = graphene.Float(input=HalfLifeInput(required=True))
    def resolve_calculate_half_life(root, info, input):
        return math.log(2) / input.k if input.k else None

    calculate_enthalpy = graphene.Float(input=EnthalpyInput(required=True))
    def resolve_calculate_enthalpy(root, info, input):
        return input.heat / input.temperature if input.temperature else None

    calculate_heat_capacity = graphene.Float(input=HeatCapacityInput(required=True))
    def resolve_calculate_heat_capacity(root, info, input):
        return input.m * input.c * input.delta_t

    calculate_nernst = graphene.Float(input=NernstInput(required=True))
    def resolve_calculate_nernst(root, info, input):
        R = 8.314
        F = 96485
        T = 298
        return input.eo - (R * T) / (input.n * F) * math.log(input.q)

    calculate_raoult = graphene.Float(input=RaoultInput(required=True))
    def resolve_calculate_raoult(root, info, input):
        return input.pure_pressure * input.solute_fraction

    calculate_henry = graphene.Float(input=HenryLawInput(required=True))
    def resolve_calculate_henry(root, info, input):
        return input.henry_constant * input.gas_pressure

    calculate_buffer_ph = graphene.Float(input=BufferInput(required=True))
    def resolve_calculate_buffer_ph(root, info, input):
        return input.pka + math.log10(input.base_concentration / input.acid_concentration)

    calculate_titration_point = graphene.Float(input=TitrationInput(required=True))
    def resolve_calculate_titration_point(root, info, input):
        return input.acid_morality * input.acid_volume / input.base_molarity if input.base_molarity else None

    calculate_freezing_point = graphene.Float(input=FreezingBoilingInput(required=True))
    def resolve_calculate_freezing_point(root, info, input):
        return -input.kf * input.m * input.i

    calculate_boiling_point = graphene.Float(input=FreezingBoilingInput(required=True))
    def resolve_calculate_boiling_point(root, info, input):
        return input.kb * input.m * input.i

    calculate_gas_diffusion = graphene.Float(input=GasDiffusionInput(required=True))
    def resolve_calculate_gas_diffusion(root, info, input):
        return math.sqrt(input.m2 / input.m1) * input.r2

    calculate_van_der_waals = graphene.Float(input=VanDerWaalsInput(required=True))
    def resolve_calculate_van_der_waals(root, info, input):
        R = 0.0821
        a = input.const_a
        b = input.const_b
        n = input.moles
        T = input.temperature
        V = input.volume
        return ((n * R * T) / (V - n * b)) - (a * n ** 2 / V ** 2)


schema = graphene.Schema(query=Query)
