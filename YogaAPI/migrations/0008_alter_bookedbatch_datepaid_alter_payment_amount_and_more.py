# Generated by Django 4.1.4 on 2022-12-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaAPI', '0007_alter_bookedbatch_phone_alter_payment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedbatch',
            name='datePaid',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(blank=True, default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datePaid',
            field=models.DateField(),
        ),
    ]
