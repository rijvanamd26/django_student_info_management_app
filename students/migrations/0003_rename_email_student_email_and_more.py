# Generated by Django 4.1 on 2022-08-14 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_gps_student_gpa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Student_number',
            new_name='student_number',
        ),
    ]