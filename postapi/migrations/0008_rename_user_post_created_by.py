# Generated by Django 3.2.4 on 2022-05-22 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0007_auto_20220521_0715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='created_by',
        ),
    ]
