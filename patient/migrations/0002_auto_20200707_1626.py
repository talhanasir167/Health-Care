# Generated by Django 2.1.5 on 2020-07-07 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctorinfo_category'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disease',
            new_name='Disease1',
        ),
    ]
