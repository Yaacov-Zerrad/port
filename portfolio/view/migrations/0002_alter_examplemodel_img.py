# Generated by Django 4.1 on 2022-08-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='img',
            field=models.ImageField(blank=True, height_field=150, upload_to='images/', width_field=200),
        ),
    ]
