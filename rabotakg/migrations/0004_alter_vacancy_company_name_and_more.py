# Generated by Django 4.1 on 2023-05-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabotakg', '0003_alter_vacancy_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
    ]