# Generated by Django 3.0.2 on 2020-07-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobs_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
