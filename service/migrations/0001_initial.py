# Generated by Django 4.2.3 on 2023-08-06 05:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان', max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, help_text='اسلاگ', unique=True, verbose_name='اسلاگ')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, help_text='ایجاد شده', verbose_name='ایجاد شده')),
                ('description', models.TextField(help_text='توضیحات اضافی', verbose_name='توضیحات اضافی')),
                ('category_cover', models.ImageField(blank=True, null=True, upload_to='category/pic/', verbose_name='تصویر')),
                ('alt_cover', models.ImageField(blank=True, null=True, upload_to='category/alt/', verbose_name='جایگزین تصویر')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, unique=True, verbose_name='اسلاگ')),
                ('pic', models.ImageField(upload_to='gallery/pic/', verbose_name='تصویر')),
                ('alt_pic', models.ImageField(upload_to='gallery/alt/', verbose_name='جایگزین تصویر')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256, verbose_name='پست الکترونیکی')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AllService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان', max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, help_text='اسلاگ', unique=True, verbose_name='اسلاگ')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, help_text='ایجاد شده', verbose_name='ایجاد شده')),
                ('description', models.TextField(help_text='توضیحات اضافی', verbose_name='توضیحات اضافی')),
                ('price', models.CharField(help_text='هزینه', max_length=12, validators=[django.core.validators.RegexValidator('^[0-9a]*$', message='Only numbers are allowed.')], verbose_name='هزینه')),
                ('service_cover', models.ImageField(blank=True, null=True, upload_to='service/pic/', verbose_name='تصویر')),
                ('alt_cover', models.ImageField(blank=True, null=True, upload_to='service/alt/', verbose_name='جایگزین تصویر')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
