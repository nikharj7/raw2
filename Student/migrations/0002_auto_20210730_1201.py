# Generated by Django 3.2.3 on 2021-07-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='University_City',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='University_Country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='University_Pin_Code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='University_State',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='University_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='University_address2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
