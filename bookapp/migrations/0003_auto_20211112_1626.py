# Generated by Django 3.2.9 on 2021-11-12 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_alter_contactid_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactid',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contactid',
            name='date_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactid',
            name='notes',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactid',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Неверный формат телефона! Введите корректное значение.e.g. +380933618505', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
