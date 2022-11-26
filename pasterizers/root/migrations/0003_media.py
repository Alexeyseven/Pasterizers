# Generated by Django 2.2.16 on 2022-11-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20221115_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Название произведения', verbose_name='Название')),
                ('actors', models.ManyToManyField(to='root.Persons')),
            ],
        ),
    ]
