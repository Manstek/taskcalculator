# Generated by Django 4.2.16 on 2024-11-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField(help_text='Введите данные в табличном формате через пробел.', verbose_name='Входные данные')),
                ('td', models.IntegerField(verbose_name='Диррективное время')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
