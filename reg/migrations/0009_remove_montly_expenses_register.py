# Generated by Django 3.2 on 2021-04-19 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0008_rename_customer_montly_expenses_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='montly_expenses',
            name='register',
        ),
    ]
