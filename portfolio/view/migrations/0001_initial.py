# Generated by Django 4.1 on 2022-08-08 19:39

from django.db import migrations, models
import view.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, upload_to='Example/')),
                ('slug_auto', models.SlugField(blank=True)),
                ('url', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IndexPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_masthead', models.CharField(max_length=255)),
                ('description_masthead', models.TextField()),
                ('title_service', models.CharField(max_length=255)),
                ('description_about', models.TextField()),
                ('title_about', models.CharField(max_length=255)),
                ('title_befor_fotter', models.CharField(max_length=255)),
                ('button_befor_fotter', models.CharField(max_length=555)),
                ('date_create', view.models.CustomDateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
            ],
        ),
    ]