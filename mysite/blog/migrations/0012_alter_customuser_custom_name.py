# Generated by Django 5.0 on 2024-01-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_customuser_custom_name_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='custom_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]