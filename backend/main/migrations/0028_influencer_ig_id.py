# Generated by Django 3.1.6 on 2021-05-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_instagram_user_profile_analysed'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='ig_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
