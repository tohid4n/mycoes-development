# Generated by Django 4.2.6 on 2023-11-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_e_offermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_offermodel',
            name='accept',
            field=models.BooleanField(),
        ),
    ]