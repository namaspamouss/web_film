# Generated by Django 2.1.5 on 2019-02-07 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webfilm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acteurs',
            name='role',
        ),
        migrations.RemoveField(
            model_name='films',
            name='role',
        ),
        migrations.DeleteModel(
            name='Acteurs',
        ),
        migrations.DeleteModel(
            name='Films',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]