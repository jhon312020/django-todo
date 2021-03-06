# Generated by Django 2.1.1 on 2019-03-29 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
            options={
                'db_table': 'tododemo',
            },
        ),
    ]
