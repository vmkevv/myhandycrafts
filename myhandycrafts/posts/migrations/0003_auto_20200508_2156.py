# Generated by Django 2.2.10 on 2020-05-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200505_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]