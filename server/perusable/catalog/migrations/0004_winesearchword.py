# Generated by Django 3.0.1 on 2019-12-24 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_update_search_vector'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineSearchWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]