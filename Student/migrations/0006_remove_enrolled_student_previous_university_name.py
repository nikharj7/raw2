# Generated by Django 3.2.3 on 2021-08-03 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_rename_student_enrolled_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolled_student',
            name='Previous_University_Name',
        ),
    ]
