# Generated by Django 4.2.1 on 2023-05-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_image_alter_event_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='event_images'),
        ),
    ]
