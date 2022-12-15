# Generated by Django 4.1.4 on 2022-12-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaAPI', '0018_alter_payment_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedbatch',
            old_name='datePaid',
            new_name='slotBooked',
        ),
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.CharField(blank=True, choices=[('1234567890', '1234567890'), ('7071955971', '7071955971'), ('7071955972', '7071955972'), ('7071955973', '7071955973'), ('7071955975', '7071955975'), ('7071955977', '7071955977')], max_length=10, null=True),
        ),
    ]