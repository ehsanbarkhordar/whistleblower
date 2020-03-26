# Generated by Django 3.0.3 on 2020-03-26 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(db_index=True, max_length=32, unique=True)),
                ('reporter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='شماره تلفن شما باید در قالب 0930******* باشد.', regex='^(\\+98|0)?9\\d{9}$')])),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('UNREAD', 'خوانده نشده'), ('SEEN', 'دیده شده'), ('ONGOING', 'در دست اقدام'), ('ACTED', 'اقدام شده')], default='خوانده نشده', max_length=50)),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]