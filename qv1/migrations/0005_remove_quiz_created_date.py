# Generated by Django 3.0.2 on 2020-02-06 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qv1', '0004_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='created_date',
        ),
    ]