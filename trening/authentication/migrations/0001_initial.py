# Generated by Django 3.0.1 on 2020-01-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('passrd', models.CharField(max_length=40)),
                ('birthday', models.DateField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
