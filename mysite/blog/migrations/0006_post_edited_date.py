# Generated by Django 5.0 on 2024-01-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
