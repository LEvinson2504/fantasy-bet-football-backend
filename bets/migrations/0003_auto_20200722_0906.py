# Generated by Django 2.2.14 on 2020-07-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_auto_20200722_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bets',
            name='away_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bets',
            name='home_points',
            field=models.IntegerField(default=0),
        ),
    ]
