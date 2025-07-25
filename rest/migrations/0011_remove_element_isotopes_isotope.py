# Generated by Django 5.1.5 on 2025-07-21 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_rename_electron_egativity_element_electronegativity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='isotopes',
        ),
        migrations.CreateModel(
            name='Isotope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('mass', models.FloatField()),
                ('abundance', models.FloatField(blank=True, null=True)),
                ('half_life', models.CharField(blank=True, max_length=50, null=True)),
                ('decay_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isotopes', to='rest.element')),
            ],
            options={
                'unique_together': {('element', 'symbol')},
            },
        ),
    ]
