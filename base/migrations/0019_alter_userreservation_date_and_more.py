# Generated by Django 4.1 on 2022-09-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_contact_usercontact_userreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
