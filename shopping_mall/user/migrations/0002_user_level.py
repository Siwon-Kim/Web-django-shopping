# Generated by Django 4.0.3 on 2022-03-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8),
            preserve_default=False,
        ),
    ]
