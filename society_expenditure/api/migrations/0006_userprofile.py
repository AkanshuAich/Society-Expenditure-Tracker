# Generated by Django 5.0 on 2023-12-27 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_content_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fats', models.BooleanField(default=False)),
                ('cult', models.BooleanField(default=False)),
                ('paracosm', models.BooleanField(default=False)),
                ('photogeeks', models.BooleanField(default=False)),
                ('tech', models.BooleanField(default=False)),
                ('vedant', models.BooleanField(default=False)),
                ('megaheartz', models.BooleanField(default=False)),
                ('tars', models.BooleanField(default=False)),
                ('ecell', models.BooleanField(default=False)),
                ('sports', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
