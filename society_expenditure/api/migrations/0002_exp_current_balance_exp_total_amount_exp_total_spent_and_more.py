# Generated by Django 5.0 on 2023-12-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exp',
            name='Current_Balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='exp',
            name='Total_Amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='exp',
            name='Total_Spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='exp',
            name='event',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='exp',
            name='name',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
