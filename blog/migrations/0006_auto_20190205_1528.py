# Generated by Django 2.1.5 on 2019-02-05 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190205_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]