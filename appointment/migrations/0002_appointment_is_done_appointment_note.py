# Generated by Django 4.1.5 on 2023-02-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
