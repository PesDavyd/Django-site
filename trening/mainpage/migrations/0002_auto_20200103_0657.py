# Generated by Django 3.0.1 on 2020-01-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_login',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=['2020', '01', '03']),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='2020', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default=('2020', '01', '03'), max_length=20),
            preserve_default=False,
        ),
    ]