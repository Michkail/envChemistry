from django.db import models


class Element(models.Model):
    from django.db import models

class Element(models.Model):
    BLOCK_CHOICES = [
        ('s', 'S Block'),
        ('p', 'P Block'), 
        ('d', 'D Block'),
        ('f', 'F Block'),
    ]

    PHASE_CHOICES = [
        ('Solid', 'Solid'),
        ('Liquid', 'Liquid'),
        ('Gas', 'Gas'),
        ('Unknown', 'Unknown'),
        ('Predicted Solid', 'Predicted Solid'),
        ('Predicted Liquid', 'Predicted Liquid'),
        ('Predicted Gas', 'Predicted Gas'),
    ]

    atomic_number = models.PositiveSmallIntegerField(unique=True)
    atomic_mass = models.FloatField()
    atomic_radius = models.FloatField()
    covalent_radius = models.FloatField()
    van_der_waals_radius = models.FloatField()
    symbol = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    period = models.PositiveSmallIntegerField()
    group = models.PositiveSmallIntegerField(null=True, blank=True)
    block = models.CharField(max_length=1, choices=BLOCK_CHOICES)
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    density = models.FloatField(null=True, blank=True)
    melting_point = models.FloatField(null=True, blank=True)
    boiling_point = models.FloatField(null=True, blank=True)
    electron_configuration = models.CharField(max_length=100, null=True, blank=True)
    electronegativity = models.FloatField(null=True, blank=True)
    electron_affinity = models.FloatField(null=True, blank=True)
    electrical_conductivity = models.FloatField(null=True, blank=True)
    thermal_conductivity = models.FloatField(null=True, blank=True)
    ionization_energy = models.FloatField(null=True, blank=True)
    oxidation_state = models.JSONField(default=list)
    abundance_earth_crust = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    abundance_universe = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    specific_heat = models.FloatField(null=True, blank=True)
    appearance = models.CharField(max_length=100, null=True, blank=True)
    crystal_structure = models.CharField(max_length=100, null=True, blank=True)
    discovery_year = models.IntegerField(null=True, blank=True)
    discovery_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Isotope(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='isotopes')
    symbol = models.CharField(max_length=10)
    mass = models.FloatField()
    abundance = models.FloatField(null=True, blank=True)
    half_life = models.CharField(max_length=50, null=True, blank=True)
    decay_mode = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ('element', 'symbol')

    def __str__(self):
        return self.symbol


class Compound(models.Model):
    name = models.CharField(max_length=100)
    chemical_formula = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    bond_type = models.CharField(max_length=50)
    properties = models.TextField()
    uses = models.TextField()
    status = models.CharField(max_length=30)
    discovery_date = models.DateField(null=True, blank=True)
    discovery_period = models.CharField(max_length=50, null=True, blank=True)
    discovery_by = models.CharField(max_length=70, null=True, blank=True)
    source = models.TextField()

    def __str__(self):
        return self.name


class CompoundElement(models.Model):
    compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.compound.name} - {self.element.name}"
