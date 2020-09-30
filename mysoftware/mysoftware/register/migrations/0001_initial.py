# Generated by Django 2.2.6 on 2020-01-25 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=8)),
                ('lastName', models.CharField(max_length=6)),
                ('age', models.IntegerField(default=-1)),
                ('email', models.EmailField(max_length=10)),
                ('userName', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(choices=[('hyd', 'HYDERABAD'), ('bang', 'BANGALORE'), ('mum', 'MUMBAI'), ('che', 'CHENNAI')], default='hyd', max_length=6)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]