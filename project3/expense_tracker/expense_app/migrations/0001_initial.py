# Generated by Django 2.0.6 on 2018-10-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
            ],
        ),
    ]
