# Generated by Django 3.1.2 on 2020-11-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('objet', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
