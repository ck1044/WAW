# Generated by Django 3.1.2 on 2020-11-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hash_tag2',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
