# Generated by Django 4.1 on 2022-08-14 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papaya', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brands',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='vehicles',
            old_name='created',
            new_name='created_at',
        ),
    ]
