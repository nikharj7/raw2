# Generated by Django 3.2.3 on 2021-08-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0002_alter_student_activity_email_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_activity_email',
            name='Certificate',
            field=models.FileField(upload_to='Student_Certificate'),
        ),
    ]
