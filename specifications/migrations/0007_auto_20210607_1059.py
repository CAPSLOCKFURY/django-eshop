# Generated by Django 3.1.7 on 2021-06-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0006_specificationpreset_is_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificationpreset',
            name='is_filter',
            field=models.BooleanField(default=True),
        ),
    ]
