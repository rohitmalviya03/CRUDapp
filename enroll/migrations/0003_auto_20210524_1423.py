# Generated by Django 3.1.5 on 2021-05-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_auto_20210524_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='name',
        ),
    ]
