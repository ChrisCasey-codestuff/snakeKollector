# Generated by Django 4.2 on 2023-04-07 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SnekToy',
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={},
        ),
    ]