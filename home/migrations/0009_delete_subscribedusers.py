# Generated by Django 4.2.3 on 2023-08-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_subscribedusers_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubscribedUsers',
        ),
    ]
