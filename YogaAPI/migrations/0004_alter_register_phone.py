# Generated by Django 4.1.4 on 2022-12-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YogaAPI', '0003_alter_batch_batch_alter_bookedbatch_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
