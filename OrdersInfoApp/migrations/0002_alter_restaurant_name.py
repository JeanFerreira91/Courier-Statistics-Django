# Generated by Django 4.0.4 on 2022-05-31 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrdersInfoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
