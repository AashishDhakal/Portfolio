# Generated by Django 3.0.5 on 2020-04-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200412_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]