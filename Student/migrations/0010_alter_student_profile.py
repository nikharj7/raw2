# Generated by Django 3.2.3 on 2021-08-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_alter_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Profile',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to='Student_Profile_Picture'),
        ),
    ]
