# Generated by Django 2.0.1 on 2018-01-14 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attero', '0010_auto_20180110_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view_project', 'Can view Project'),)},
        ),
    ]
