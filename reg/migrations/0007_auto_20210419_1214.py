# Generated by Django 3.2 on 2021-04-19 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_register_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
        migrations.AddField(
            model_name='montly_expenses',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reg.register'),
        ),
    ]
