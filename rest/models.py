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
