# Generated by Django 4.0.3 on 2022-04-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_servicecategory_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directioncategory',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='directioncategory',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
