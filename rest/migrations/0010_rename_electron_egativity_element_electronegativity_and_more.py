# Generated by Django 5.1.5 on 2025-07-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_element_abundance_earth_crust_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='electron_egativity',
            new_name='electronegativity',
        ),
        migrations.RemoveField(
            model_name='element',
            name='crystalStructure',
        ),
        migrations.AddField(
            model_name='element',
            name='crystal_structure',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='appearance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='atomic_number',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='covalent_radius',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='element',
            name='electron_configuration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='period',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='element',
            name='phase',
            field=models.CharField(choices=[('Solid', 'Solid'), ('Liquid', 'Liquid'), ('Gas', 'Gas'), ('Unknown', 'Unknown'), ('Predicted Solid', 'Predicted Solid'), ('Predicted Liquid', 'Predicted Liquid'), ('Predicted Gas', 'Predicted Gas')], max_length=20),
        ),
        migrations.AlterField(
            model_name='element',
            name='specific_heat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='van_der_waals_radius',
            field=models.FloatField(),
        ),
    ]
