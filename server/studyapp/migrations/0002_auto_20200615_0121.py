# Generated by Django 3.0.6 on 2020-06-14 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='study',
            old_name='category_id',
            new_name='category',
        ),
    ]