# Generated by Django 3.2.8 on 2021-10-15 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Images',
            new_name='images',
        ),
    ]
