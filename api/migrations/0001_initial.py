# Generated by Django 4.0.3 on 2022-04-08 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField()),
                ('file', models.FileField(upload_to='uploads/application')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1000)),
                ('address_uz', models.CharField(max_length=1000, null=True)),
                ('address_en', models.CharField(max_length=1000, null=True)),
                ('address_ru', models.CharField(max_length=1000, null=True)),
                ('phone_number', models.CharField(max_length=400)),
                ('foundation_date', models.DateTimeField()),
                ('clients_number', models.IntegerField()),
                ('employee_number', models.IntegerField()),
                ('projects_number', models.IntegerField()),
                ('technical_support', models.IntegerField()),
                ('icon', models.ImageField(upload_to='uploads/contact')),
                ('short_video', models.FileField(upload_to='uploads/contact')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='DirectionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='uploads/direction')),
                ('background_image', models.ImageField(upload_to='uploads/direction')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'direction_category',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('first_name_uz', models.CharField(max_length=255, null=True)),
                ('first_name_en', models.CharField(max_length=255, null=True)),
                ('first_name_ru', models.CharField(max_length=255, null=True)),
                ('second_name', models.CharField(max_length=255)),
                ('second_name_uz', models.CharField(max_length=255, null=True)),
                ('second_name_en', models.CharField(max_length=255, null=True)),
                ('second_name_ru', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(upload_to='uploads/employee')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='MainPageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_title', models.CharField(max_length=200)),
                ('logo_title_uz', models.CharField(max_length=200, null=True)),
                ('logo_title_en', models.CharField(max_length=200, null=True)),
                ('logo_title_ru', models.CharField(max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='uploads/settings')),
                ('poster_title', models.CharField(max_length=200)),
                ('poster_title_uz', models.CharField(max_length=200, null=True)),
                ('poster_title_en', models.CharField(max_length=200, null=True)),
                ('poster_title_ru', models.CharField(max_length=200, null=True)),
                ('poster_description', models.CharField(max_length=500)),
                ('poster_description_uz', models.CharField(max_length=500, null=True)),
                ('poster_description_en', models.CharField(max_length=500, null=True)),
                ('poster_description_ru', models.CharField(max_length=500, null=True)),
                ('instagram_link', models.URLField()),
                ('facebook_link', models.URLField()),
                ('telegram_link', models.URLField()),
                ('icon', models.ImageField(upload_to='uploads/settings')),
                ('rocket_icon', models.ImageField(upload_to='uploads/settings')),
                ('poster_image_web', models.ImageField(upload_to='uploads/settings')),
                ('poster_image_mobile', models.ImageField(upload_to='uploads/settings')),
                ('poster_image_planshet', models.ImageField(upload_to='uploads/settings')),
                ('second_poster_image', models.ImageField(upload_to='uploads/settings')),
                ('second_poster_description', models.CharField(max_length=500)),
                ('second_poster_description_uz', models.CharField(max_length=500, null=True)),
                ('second_poster_description_en', models.CharField(max_length=500, null=True)),
                ('second_poster_description_ru', models.CharField(max_length=500, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_uz', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('link', models.URLField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'partner',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_category',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='uploads/service')),
                ('icon', models.ImageField(upload_to='uploads/service')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'service_category',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('icon', models.ImageField(upload_to='uploads/direction')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('direction_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='api.directioncategory')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('icon', models.ImageField(upload_to='uploads/stage')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='api.servicecategory')),
            ],
            options={
                'db_table': 'stage',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('logo', models.ImageField(upload_to='uploads/service')),
                ('icon', models.ImageField(upload_to='uploads/service')),
                ('image', models.ImageField(upload_to='uploads/service')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='api.servicecategory')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_uz', models.CharField(max_length=500, null=True)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('title_ru', models.CharField(max_length=500, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/project')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='api.projectcategory')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField(null=True)),
                ('url', models.CharField(max_length=255)),
                ('is_footer', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='api.menu')),
            ],
            options={
                'db_table': 'menu',
                'ordering': ['order'],
            },
        ),
    ]