import json
from rest.models import Element, CompoundElement, Compound


sodium = Element.objects.get(symbol="Na")
chlorine = Element.objects.get(symbol="Cl")
hydrogen = Element.objects.get(symbol="H")
oxygen = Element.objects.get(symbol="O")
carbon = Element.objects.get(symbol="C")
sulfur = Element.objects.get(symbol="S")
nitrogen = Element.objects.get(symbol="N")
calcium = Element.objects.get(symbol="Ca")
fluorine = Element.objects.get(symbol="F")
phosphorus = Element.objects.get(symbol="P")

# with open('repositories/compound.json') as f:
#     compound = json.load(f)
#     print(compound)
#
#     for i in compound:
#         Compound.objects.create(**i)
#

compounds_data = [
    {
        "name": "Water",
        "chemical_formula": "H2O",
        "category": "Inorganic",
        "bond_type": "Covalent",
        "properties": "Colorless, tasteless liquid, essential for life",
        "uses": "Drinking, industrial cooling, chemical solvent",
        "status": "Natural",
        "discovery_date": None,
        "discovery_period": "Ancient",
        "discovery_by": None,
        "source": "Oceans, rivers, lakes",
        "elements": [hydrogen, oxygen]
    },
    {
        "name": "Methane",
        "chemical_formula": "CH4",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Colorless, odorless gas, main component of natural gas",
        "uses": "Fuel, chemical feedstock",
        "status": "Natural",
        "discovery_date": "1776-01-01",
        "discovery_period": "18th century",
        "discovery_by": "Alessandro Volta",
        "source": "Natural gas, biological processes",
        "elements": [carbon, hydrogen]
    },
    {
        "name": "Glucose",
        "chemical_formula": "C6H12O6",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Simple sugar, energy source for cells",
        "uses": "Food, metabolism, medical applications",
        "status": "Natural",
        "discovery_date": "1838-01-01",
        "discovery_period": "19th century",
        "discovery_by": "Jean Baptiste Dumas & Jean-Baptiste André Dumas",
        "source": "Plants (photosynthesis), blood sugar",
        "elements": [carbon, hydrogen, oxygen]
    },
    {
        "name": "Ammonia",
        "chemical_formula": "NH3",
        "category": "Inorganic",
        "bond_type": "Covalent",
        "properties": "Pungent-smelling gas, soluble in water",
        "uses": "Fertilizers, cleaning agents, industrial refrigerant",
        "status": "Natural and synthetic",
        "discovery_date": "1774-01-01",
        "discovery_period": "18th century",
        "discovery_by": "Joseph Priestley",
        "source": "Nitrogen fixation, industrial production",
        "elements": [nitrogen, hydrogen]
    },
    {
        "name": "Calcium Carbonate",
        "chemical_formula": "CaCO3",
        "category": "Inorganic",
        "bond_type": "Ionic",
        "properties": "White solid, forms limestone and marble",
        "uses": "Building materials, antacid, chalk",
        "status": "Natural",
        "discovery_date": None,
        "discovery_period": "Ancient",
        "discovery_by": None,
        "source": "Rocks, shells, corals",
        "elements": [calcium, carbon, oxygen]
    },
    {
        "name": "Ethanol",
        "chemical_formula": "C2H5OH",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Volatile, flammable liquid, used in alcoholic beverages",
        "uses": "Solvent, fuel, disinfectant, alcoholic drinks",
        "status": "Natural and synthetic",
        "discovery_date": "9000-01-01",
        "discovery_period": "Ancient",
        "discovery_by": "Ancient civilizations",
        "source": "Fermentation of sugars",
        "elements": [carbon, hydrogen, oxygen]
    },
    {
        "name": "Tetrahydrocannabinol",
        "chemical_formula": "C21H30O2",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Psychoactive compound in cannabis, fat-soluble",
        "uses": "Medical treatment for pain, nausea, recreational drug",
        "status": "Synthetic and natural",
        "discovery_date": "1964-01-01",
        "discovery_period": "20th century",
        "discovery_by": "Raphael Mechoulam",
        "source": "Cannabis sativa",
        "elements": [carbon, hydrogen, oxygen]
    },
    {
        "name": "Sodium Chloride",
        "chemical_formula": "NaCl",
        "category": "Inorganic",
        "bond_type": "Ionic",
        "properties": "White crystalline solid, soluble in water",
        "uses": "Used as table salt, food preservative",
        "status": "Natural",
        "discovery_date": None,
        "discovery_period": "Ancient",
        "discovery_by": None,
        "source": "Seawater, rock salt",
        "elements": [sodium, chlorine]
    },
    {
        "name": "Carbon Dioxide",
        "chemical_formula": "CO2",
        "category": "Inorganic",
        "bond_type": "Covalent",
        "properties": "Colorless gas, heavier than air",
        "uses": "Used in carbonated drinks, fire extinguishers, photosynthesis",
        "status": "Natural",
        "discovery_date": "1754-01-01",
        "discovery_period": None,
        "discovery_by": "Joseph Black",
        "source": "Atmosphere, respiration",
        "elements": [carbon, oxygen]
    },
    {
        "name": "Sulfuric Acid",
        "chemical_formula": "H2SO4",
        "category": "Inorganic",
        "bond_type": "Covalent",
        "properties": "Corrosive liquid, highly reactive",
        "uses": "Used in batteries, fertilizers, chemical synthesis",
        "status": "Synthetic",
        "discovery_date": None,
        "discovery_period": "Medieval",
        "discovery_by": "Jabir ibn Hayyan",
        "source": "Industrial production",
        "elements": [hydrogen, sulfur, oxygen]
    },
    {
        "name": "Mustard Gas (Yperite)",
        "chemical_formula": "C4H8Cl2S",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Oily liquid, blistering agent, highly toxic",
        "uses": "Chemical warfare agent",
        "status": "Synthetic",
        "discovery_date": "1822-01-01",
        "discovery_period": None,
        "discovery_by": "César-Mansuète Despretz",
        "source": "Synthetic production",
        "elements": [carbon, hydrogen, chlorine, sulfur]
    },
    {
        "name": "Phosgene",
        "chemical_formula": "COCl2",
        "category": "Inorganic",
        "bond_type": "Covalent",
        "properties": "Colorless gas, toxic, used as a chemical weapon",
        "uses": "Chemical warfare, industrial chemical synthesis",
        "status": "Synthetic",
        "discovery_date": "1812-01-01",
        "discovery_period": None,
        "discovery_by": "John Davy",
        "source": "Synthetic production",
        "elements": [carbon, oxygen, chlorine]
    },
    {
        "name": "Sarin",
        "chemical_formula": "C4H10FO2P",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Highly toxic nerve agent, volatile",
        "uses": "Chemical warfare nerve agent",
        "status": "Synthetic",
        "discovery_date": "1938-01-01",
        "discovery_period": None,
        "discovery_by": "Gerhard Schrader",
        "source": "Synthetic production",
        "elements": [carbon, hydrogen, fluorine, oxygen, phosphorus]
    },
    {
        "name": "Soman",
        "chemical_formula": "C7H16FO2P",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Highly toxic nerve agent, more persistent than Sarin",
        "uses": "Chemical warfare nerve agent",
        "status": "Synthetic",
        "discovery_date": "1944-01-01",
        "discovery_period": None,
        "discovery_by": "Richard Kuhn",
        "source": "Synthetic production",
        "elements": [carbon, hydrogen, fluorine, oxygen, phosphorus]
    },
    {
        "name": "VX",
        "chemical_formula": "C11H26NO2PS",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Extremely toxic nerve agent, persistent",
        "uses": "Chemical warfare nerve agent",
        "status": "Synthetic",
        "discovery_date": "1952-01-01",
        "discovery_period": None,
        "discovery_by": "Ranajit Ghosh",
        "source": "Synthetic production",
        "elements": [carbon, hydrogen, nitrogen, oxygen, phosphorus, sulfur]
    },
    {
        "name": "Novichok Agents",
        "chemical_formula": "Varies (A-series nerve agents)",
        "category": "Organic",
        "bond_type": "Covalent",
        "properties": "Highly toxic nerve agent, more potent than VX",
        "uses": "Chemical warfare nerve agent",
        "status": "Synthetic",
        "discovery_date": "1970-01-01",
        "discovery_period": None,
        "discovery_by": "Soviet scientists",
        "source": "Synthetic production",
        "elements": [carbon, hydrogen, nitrogen, oxygen, phosphorus]
    }
]

for data in compounds_data:
    compound = Compound.objects.create(
        name=data["name"],
        chemical_formula=data["chemical_formula"],
        category=data["category"],
        bond_type=data["bond_type"],
        properties=data["properties"],
        uses=data["uses"],
        status=data["status"],
        discovery_date=data["discovery_date"],
        discovery_period=data["discovery_period"],
        discovery_by=data["discovery_by"],
        source=data["source"]
    )

    for element in data["elements"]:
        CompoundElement.objects.create(compound=compound, element=element)

print("All compounds inserted successfully!")
