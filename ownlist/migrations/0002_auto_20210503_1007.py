# Generated by Django 3.1.6 on 2021-05-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='nAddress',
            new_name='sDate',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nBreed',
            new_name='sEaddress',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nDay',
            new_name='sFname',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nname',
            new_name='sLname',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='npet',
            new_name='sNumber',
        ),
        migrations.AddField(
            model_name='item',
            name='sPlace',
            field=models.TextField(default=''),
        ),
    ]
