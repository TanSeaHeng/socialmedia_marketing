# Generated by Django 3.1.6 on 2021-03-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_influencer_api_connect_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='negative_keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
