# Generated by Django 3.1.2 on 2020-11-14 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_parts', '0002_auto_20201114_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_parts.famillepiece'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_parts.marquepiece'),
        ),
    ]
