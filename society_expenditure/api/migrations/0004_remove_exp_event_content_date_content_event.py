# Generated by Django 5.0 on 2023-12-25 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_name_exp_user_name_remove_exp_current_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exp',
            name='event',
        ),
        migrations.AddField(
            model_name='content',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 12, 24)),
        ),
        migrations.AddField(
            model_name='content',
            name='event',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
