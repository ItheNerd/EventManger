# Generated by Django 4.2.1 on 2023-05-29 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_image_event_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image_url',
            new_name='image',
        ),
    ]