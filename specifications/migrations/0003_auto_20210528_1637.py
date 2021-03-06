# Generated by Django 3.1.7 on 2021-05-28 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0002_categoryspecifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specification',
            old_name='name',
            new_name='spec_name',
        ),
        migrations.AlterField(
            model_name='categoryspecifications',
            name='spec_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='specifications.specificationpreset'),
        ),
    ]
