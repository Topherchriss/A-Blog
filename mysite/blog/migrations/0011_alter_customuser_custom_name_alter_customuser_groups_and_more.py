# Generated by Django 5.0 on 2024-01-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0010_alter_customuser_custom_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='custom_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_users', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_users', related_query_name='custom_user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]