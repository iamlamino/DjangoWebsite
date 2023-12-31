# Generated by Django 4.2.3 on 2023-07-09 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_user_auth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='last authentification date'),
            preserve_default=False,
        ),
    ]
