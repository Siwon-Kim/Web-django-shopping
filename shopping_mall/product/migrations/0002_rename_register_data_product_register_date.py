# Generated by Django 4.0.3 on 2022-03-03 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='register_data',
            new_name='register_date',
        ),
    ]
