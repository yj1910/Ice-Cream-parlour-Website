# Generated by Django 4.2.3 on 2023-08-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_subscribedusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedusers',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]