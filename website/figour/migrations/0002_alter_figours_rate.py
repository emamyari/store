# Generated by Django 4.1.2 on 2022-10-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figours',
            name='rate',
            field=models.IntegerField(default=5, verbose_name='امتیاز'),
        ),
    ]