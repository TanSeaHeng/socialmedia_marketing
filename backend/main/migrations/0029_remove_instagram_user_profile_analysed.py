# Generated by Django 3.1.6 on 2021-05-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_influencer_ig_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagram_user_profile',
            name='analysed',
        ),
    ]
