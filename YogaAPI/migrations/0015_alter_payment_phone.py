# Generated by Django 4.1.4 on 2022-12-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaAPI', '0014_alter_payment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
