# Generated by Django 3.2.7 on 2021-09-30 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dpimp',
            new_name='dpimg',
        ),
    ]