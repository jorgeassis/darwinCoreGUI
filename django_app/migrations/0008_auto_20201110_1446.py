# Generated by Django 3.1.3 on 2020-11-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0007_auto_20201110_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodiversityrecords',
            name='acceptedSpeciesName',
            field=models.CharField(default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='biodiversityrecords',
            name='speciesName',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]
