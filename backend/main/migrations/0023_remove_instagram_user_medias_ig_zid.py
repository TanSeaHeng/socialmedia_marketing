# Generated by Django 3.1.6 on 2021-05-03 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210503_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagram_user_medias',
            name='ig_zid',
        ),
    ]
