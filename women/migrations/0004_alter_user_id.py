# Generated by Django 4.1.3 on 2022-11-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_user_women_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
