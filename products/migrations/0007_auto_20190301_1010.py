# Generated by Django 2.1.7 on 2019-03-01 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190227_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_active',
            new_name='active',
        ),
    ]
