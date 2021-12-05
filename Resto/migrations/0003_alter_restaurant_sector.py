# Generated by Django 3.2.9 on 2021-11-28 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resto', '0002_alter_sector_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Restaurants', to='Resto.sector'),
        ),
    ]
