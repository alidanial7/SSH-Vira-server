# Generated by Django 3.1.7 on 2021-04-12 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_auto_20210328_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'permissions': (('to_step_1', 'To step 1'), ('to_step_2', 'To step 2'), ('to_step_3', 'To step 3'))},
        ),
    ]
