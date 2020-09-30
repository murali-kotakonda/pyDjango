# Generated by Django 2.2.6 on 2020-01-24 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200124_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('currAddr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Addr')),
            ],
        ),
    ]