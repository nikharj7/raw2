# Generated by Django 3.2.3 on 2021-08-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_rename_enrolled_student_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Profile',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='Student_Profile_Picture'),
        ),
    ]
