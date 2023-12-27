# Generated by Django 5.0 on 2023-12-25 04:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_exp_current_balance_exp_total_amount_exp_total_spent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='exp',
            name='Current_Balance',
        ),
        migrations.RemoveField(
            model_name='exp',
            name='Total_Amount',
        ),
        migrations.RemoveField(
            model_name='exp',
            name='Total_Spent',
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Current_Balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('Total_Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('Total_Spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]