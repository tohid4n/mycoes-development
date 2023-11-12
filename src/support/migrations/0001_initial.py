# Generated by Django 4.2.6 on 2023-11-11 05:18

from django.db import migrations, models
import support.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalFAQ',
            fields=[
                ('id', models.CharField(default=support.models.generate_short_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('link_to', models.CharField(blank=True, max_length=100, null=True)),
                ('link_to_text', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralFAQ',
            fields=[
                ('id', models.CharField(default=support.models.generate_short_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('link_to', models.CharField(blank=True, max_length=100, null=True)),
                ('link_to_text', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricingFAQ',
            fields=[
                ('id', models.CharField(default=support.models.generate_short_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('link_to', models.CharField(blank=True, max_length=100, null=True)),
                ('link_to_text', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesFAQ',
            fields=[
                ('id', models.CharField(default=support.models.generate_short_id, editable=False, max_length=8, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('link_to', models.CharField(blank=True, max_length=100, null=True)),
                ('link_to_text', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
