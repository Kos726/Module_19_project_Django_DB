# Generated by Django 5.1.4 on 2024-12-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0007_alter_buyer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]