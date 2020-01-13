# Generated by Django 2.1.1 on 2018-12-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0005_address_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, to='addressbook.Person', verbose_name='Friends'),
        ),
    ]