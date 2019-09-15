# Generated by Django 2.2.1 on 2019-09-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetailDjango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.TextField()),
                ('cover', models.TextField()),
                ('bookinfo', models.TextField()),
                ('fullintro', models.TextField()),
                ('catalog', models.TextField()),
                ('tags', models.TextField()),
                ('seriesintro', models.TextField()),
                ('ratenum', models.CharField(max_length=255)),
                ('ratevoters', models.CharField(max_length=255)),
            ],
        ),
    ]
