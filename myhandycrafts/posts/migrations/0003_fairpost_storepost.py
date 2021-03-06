# Generated by Django 2.2.10 on 2020-05-28 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fairs', '0003_auto_20200527_2002'),
        ('stores', '0003_auto_20200527_2002'),
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='show when the object is active.', verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the objects was created.', verbose_name='create_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the objects was last updated.', verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the objects was deleted.', null=True, verbose_name='deleted_at')),
                ('created_by', models.PositiveIntegerField(help_text='created_by', null=True)),
                ('updated_by', models.PositiveIntegerField(help_text='updated_by', null=True)),
                ('deleted_by', models.PositiveIntegerField(help_text='deleted_by', null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='posts')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store', verbose_name='stores')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FairPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='show when the object is active.', verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the objects was created.', verbose_name='create_at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the objects was last updated.', verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the objects was deleted.', null=True, verbose_name='deleted_at')),
                ('created_by', models.PositiveIntegerField(help_text='created_by', null=True)),
                ('updated_by', models.PositiveIntegerField(help_text='updated_by', null=True)),
                ('deleted_by', models.PositiveIntegerField(help_text='deleted_by', null=True)),
                ('fair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fairs.Fair', verbose_name='fairs')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
