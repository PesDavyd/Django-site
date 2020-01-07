# Generated by Django 3.0.1 on 2020-01-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=120)),
                ('Post', models.TextField()),
                ('Picture', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
