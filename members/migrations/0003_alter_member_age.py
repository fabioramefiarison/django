# Generated by Django 5.1.3 on 2024-11-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(),
        ),
    ]