# Generated by Django 3.2.19 on 2023-06-02 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]