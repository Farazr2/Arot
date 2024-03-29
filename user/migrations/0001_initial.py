# Generated by Django 4.2.3 on 2023-08-06 05:13

from django.conf import settings
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(help_text='این فیلد برای احراز هویت استفاده میشود، در انتخاب آن دقت کنید', max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')], verbose_name='شماره تماس')),
                ('email', models.EmailField(help_text='این فیلد الزامی میباشد', max_length=244, unique=True, verbose_name='پست الکترونیکی')),
                ('first_name', models.CharField(blank=True, help_text='این فیلد الزامی میباشد', max_length=30, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, help_text='این فیلد الزامی میباشد', max_length=50, null=True, verbose_name='نام خانوادگی')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت فعالیت')),
                ('is_staff', models.BooleanField(default=False, verbose_name='دسترسی ادمین')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='مدیر')),
                ('joined_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='پست الکترونیکی')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام خانوادگی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
