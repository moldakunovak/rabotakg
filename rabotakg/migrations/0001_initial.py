# Generated by Django 4.1 on 2023-05-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('company_name', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(max_length=50)),
                ('contact_info', models.TextField()),
            ],
        ),
    ]