# Generated by Django 5.0.1 on 2024-02-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_pedido_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Electrónicos', 'Electrónicos'), ('Muebles', 'Muebles'), ('Electrodomésticos', 'Electrodomésticos'), ('Limpieza', 'Limpieza'), ('Comestibles', 'Comestibles')], max_length=30, null=True),
        ),
    ]
