# Generated by Django 3.2.9 on 2021-12-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tecnico',
        ),
    ]
