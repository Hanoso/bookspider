# Generated by Django 2.2.1 on 2019-09-14 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookspiderAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdetaildjango',
            old_name='cover',
            new_name='coverDjango',
        ),
    ]
