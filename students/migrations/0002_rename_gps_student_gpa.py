# Generated by Django 4.1 on 2022-08-14 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gps',
            new_name='gpa',
        ),
    ]
