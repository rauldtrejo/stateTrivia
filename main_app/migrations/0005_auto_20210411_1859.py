# Generated by Django 3.1.7 on 2021-04-11 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210409_0741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['state']},
        ),
    ]
