# Generated by Django 4.0.3 on 2022-04-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_mainpagesettings_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='logo',
        ),
    ]
