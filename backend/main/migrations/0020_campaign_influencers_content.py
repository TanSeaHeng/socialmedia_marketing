# Generated by Django 3.1.6 on 2021-04-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210412_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='influencers_content',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
