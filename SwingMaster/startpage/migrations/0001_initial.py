# Generated by Django 3.2.9 on 2021-11-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='유저 이름')),
                ('user_email', models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')),
                ('user_register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user',
            },
        ),
    ]
