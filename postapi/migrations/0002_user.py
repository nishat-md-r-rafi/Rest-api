# Generated by Django 3.2.4 on 2022-05-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=35)),
            ],
        ),
    ]
