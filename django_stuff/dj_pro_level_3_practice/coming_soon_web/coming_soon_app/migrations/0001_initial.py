# Generated by Django 4.2.6 on 2023-12-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EarlyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=164)),
                ('last_name', models.CharField(max_length=164)),
                ('email', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
