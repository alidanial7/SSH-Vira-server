# Generated by Django 3.1.7 on 2021-03-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0007_auto_20210301_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='cook_chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cook_chef', to='kitchen.chef'),
        ),
        migrations.AlterField(
            model_name='cook',
            name='preparation_chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preparation_chef', to='kitchen.chef'),
        ),
    ]
