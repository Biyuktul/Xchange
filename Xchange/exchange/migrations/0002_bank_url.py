# Generated by Django 5.1.1 on 2024-09-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='url',
            field=models.URLField(default='http://'),
            preserve_default=False,
        ),
    ]