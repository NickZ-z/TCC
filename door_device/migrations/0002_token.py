# Generated by Django 3.2.4 on 2023-12-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
            ],
        ),
    ]
