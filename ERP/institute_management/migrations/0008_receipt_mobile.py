# Generated by Django 2.2.1 on 2019-06-27 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute_management', '0007_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='Mobile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='institute_management.Admission'),
        ),
    ]
