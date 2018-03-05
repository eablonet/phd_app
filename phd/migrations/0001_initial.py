# Generated by Django 2.0 on 2018-03-04 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Substrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_treatment', models.DateTimeField(blank=True, null=True)),
                ('chimie', models.CharField(blank=True, max_length=20, null=True)),
                ('treatment_time', models.FloatField(blank=True, null=True)),
                ('oven_time', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tensiometrie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('serie', models.IntegerField(blank=True, null=True)),
                ('left', models.FloatField(blank=True, null=True)),
                ('right', models.FloatField(blank=True, null=True)),
                ('method', models.CharField(choices=[('st', 'Static'), ('ad', 'Advancing'), ('re', 'Receding')], default='st', max_length=2)),
                ('substrate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phd.Substrate')),
            ],
        ),
    ]
