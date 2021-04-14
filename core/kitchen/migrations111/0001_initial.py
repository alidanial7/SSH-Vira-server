# Generated by Django 3.1.7 on 2021-02-22 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personnel_error', models.TextField(null=True)),
                ('daily_report', models.TextField(null=True)),
                ('extra_food_number', models.IntegerField(default=0)),
                ('report_date', models.DateField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cook_chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cook_chef', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('distributor1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributor1', to=settings.AUTH_USER_MODEL)),
                ('distributor2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributor2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField(default=0)),
                ('report_date', models.DateField(null=True, unique=True)),
                ('comment', models.TextField(null=True)),
                ('cook_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.cook')),
                ('distribution_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.distribution')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.meal')),
            ],
        ),
        migrations.AddField(
            model_name='distribution',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.meal'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.section'),
        ),
        migrations.AddField(
            model_name='cook',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.food'),
        ),
        migrations.AddField(
            model_name='cook',
            name='preparation_chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preparation_chef', to=settings.AUTH_USER_MODEL),
        ),
    ]
