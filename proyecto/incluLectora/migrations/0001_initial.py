# Generated by Django 4.2.4 on 2024-02-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=100)),
                ('campo2', models.IntegerField()),
            ],
        ),
    ]