# Generated by Django 4.2 on 2023-04-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_delete_snektoy_alter_feeding_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='feeding date'),
        ),
    ]
