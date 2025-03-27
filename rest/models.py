from django.db import models


class Element(models.Model):
    atomic_number = models.IntegerField(unique=True)
    atomic_mass = models.FloatField()
    symbol = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    density = models.FloatField(null=True, blank=True)
    melting_point = models.FloatField(null=True, blank=True)
    boiling_point = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


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
