# Generated by Django 4.1.7 on 2023-03-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loyalty_program_app', '0005_remove_userprofile_invoices_invoices_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='basic_points',
            field=models.IntegerField(),
        ),
    ]
