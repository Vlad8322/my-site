# Generated by Django 3.0.3 on 2020-05-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_loadimage_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadimage',
            name='name_image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
