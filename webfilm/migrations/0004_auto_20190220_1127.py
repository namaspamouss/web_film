# Generated by Django 2.1.5 on 2019-02-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webfilm', '0003_acteurs_films_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acteurs',
            options={'verbose_name': 'acteur'},
        ),
        migrations.AlterModelOptions(
            name='films',
            options={'ordering': ['annee'], 'verbose_name': 'film'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'role'},
        ),
    ]