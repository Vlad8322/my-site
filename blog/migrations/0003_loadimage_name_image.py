# Generated by Django 3.0.3 on 2020-05-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200516_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadimage',
            name='name_image',
            field=models.TextField(default=None),
        ),
    ]