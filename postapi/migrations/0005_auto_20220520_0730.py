# Generated by Django 3.2.4 on 2022-05-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0004_auto_20220520_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]