# Generated by Django 2.2.1 on 2019-06-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute_management', '0008_receipt_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='Mobile',
            field=models.CharField(max_length=20),
        ),
    ]
