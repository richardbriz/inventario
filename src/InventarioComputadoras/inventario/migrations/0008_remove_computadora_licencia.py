# Generated by Django 5.1.3 on 2024-11-08 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_computadora_licencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadora',
            name='licencia',
        ),
    ]
