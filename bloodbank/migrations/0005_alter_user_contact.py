# Generated by Django 3.2.7 on 2021-09-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0004_auto_20210929_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
