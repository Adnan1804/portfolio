# Generated by Django 3.0.2 on 2020-07-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_certificates_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='issue',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
