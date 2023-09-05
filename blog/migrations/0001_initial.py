# Generated by Django 4.2.3 on 2023-08-06 05:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='سربرگ')),
                ('txt', models.TextField(verbose_name='دیدگاه')),
                ('admin_approval', models.BooleanField(default=False, verbose_name='تایید مدیر')),
                ('vote', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='امتیاز')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='نوشته شده در تاریخ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]