# Generated by Django 2.2.1 on 2019-06-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute_management', '0010_auto_20190628_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]