# Generated by Django 5.0 on 2024-01-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_customuser_custom_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='call_me',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
