# Generated by Django 5.0 on 2024-01-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_customuser_custom_name_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='custom_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
