# Generated by Django 3.0.3 on 2020-02-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.CharField(max_length=100)),
                ('end_day', models.CharField(max_length=100)),
                ('timing', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]