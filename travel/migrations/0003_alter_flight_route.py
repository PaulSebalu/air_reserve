# Generated by Django 3.2 on 2022-02-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20220226_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='route',
            field=models.ManyToManyField(db_table='flight_routes', related_name='routes', related_query_name='route', to='travel.Route'),
        ),
    ]
