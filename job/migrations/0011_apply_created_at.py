# Generated by Django 5.0.7 on 2024-07-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
