# Generated by Django 3.1.2 on 2020-11-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='cylindré',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='voiture',
            name='puissance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
