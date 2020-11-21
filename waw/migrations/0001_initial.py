# Generated by Django 3.1.2 on 2020-11-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_tag', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('pin', models.DecimalField(decimal_places=0, max_digits=99999999)),
            ],
        ),
    ]
