# Generated by Django 2.1.5 on 2020-07-13 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20200713_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease1',
            old_name='name',
            new_name='disease_name',
        ),
        migrations.RenameField(
            model_name='disease1',
            old_name='category',
            new_name='doctor_name',
        ),
    ]
