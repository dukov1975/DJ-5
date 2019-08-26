# Generated by Django 2.2.2 on 2019-08-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chinaphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=50, verbose_name='Модель')),
                ('phone_type', models.CharField(max_length=10, verbose_name='Тип')),
                ('phone_form', models.CharField(max_length=15, verbose_name='Форм-фактор')),
                ('gsm_900_1800', models.BooleanField(max_length=10, verbose_name='GSM 900/1800')),
                ('gsm_1900', models.BooleanField(max_length=10, verbose_name='GSM 1900')),
                ('gsm_3g', models.BooleanField(max_length=10, verbose_name='3G')),
                ('sim_type', models.CharField(max_length=10, verbose_name='Тип SIM')),
                ('OS', models.CharField(max_length=10, verbose_name='ОС')),
                ('mem_card', models.CharField(max_length=10, verbose_name='Карта памяти')),
                ('radio', models.BooleanField(max_length=10, verbose_name='FM-модуль')),
                ('sim_quantity', models.IntegerField(verbose_name='Количество SIM')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Iphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=50, verbose_name='Модель')),
                ('phone_type', models.CharField(max_length=10, verbose_name='Тип')),
                ('phone_form', models.CharField(max_length=15, verbose_name='Форм-фактор')),
                ('gsm_900_1800', models.BooleanField(max_length=10, verbose_name='GSM 900/1800')),
                ('gsm_1900', models.BooleanField(max_length=10, verbose_name='GSM 1900')),
                ('gsm_3g', models.BooleanField(max_length=10, verbose_name='3G')),
                ('sim_type', models.CharField(max_length=10, verbose_name='Тип SIM')),
                ('OS', models.CharField(max_length=10, verbose_name='ОС')),
                ('animoji', models.BooleanField(max_length=10, verbose_name='Поддержка Animoji')),
                ('imessage', models.BooleanField(max_length=10, verbose_name='Поддержка iMessage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
