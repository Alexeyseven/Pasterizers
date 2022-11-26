# Generated by Django 2.2.16 on 2022-11-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('name', models.TextField(help_text='Имя сотрудника', verbose_name='Имя')),
                ('sirname', models.TextField(help_text='Фамилия сотрудника', verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employes',
            },
        ),
    ]
