# Generated by Django 5.1.4 on 2024-12-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0006_alter_buyer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
