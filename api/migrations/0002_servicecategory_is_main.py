# Generated by Django 4.0.3 on 2022-04-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
