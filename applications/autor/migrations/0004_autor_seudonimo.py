# Generated by Django 3.1.7 on 2021-03-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0003_auto_20210321_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='seudonimo',
            field=models.CharField(blank=True, max_length=50, verbose_name='seudonimo'),
        ),
    ]
