# Generated by Django 5.1.5 on 2025-03-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_alter_compound_discovery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='discovery_period',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
