# Generated by Django 4.1.4 on 2022-12-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaAPI', '0009_alter_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedbatch',
            name='slot',
            field=models.CharField(blank=True, choices=[('5AM-6AM', '5AM-6AM'), ('6AM-7AM', '6AM-7AM'), ('7AM-8AM', '7AM-8AM'), ('8AM-9AM', '8AM-9AM')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(blank=True, default='000'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentId',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
