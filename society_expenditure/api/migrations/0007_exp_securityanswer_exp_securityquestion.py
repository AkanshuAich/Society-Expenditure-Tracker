# Generated by Django 5.0 on 2023-12-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='exp',
            name='securityanswer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='exp',
            name='securityquestion',
            field=models.CharField(default='', max_length=100),
        ),
    ]