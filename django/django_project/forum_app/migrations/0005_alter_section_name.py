# Generated by Django 5.0.6 on 2024-05-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0004_alter_message_message_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.TextField(max_length=100, unique=True, verbose_name='name'),
        ),
    ]
