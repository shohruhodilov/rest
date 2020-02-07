# Generated by Django 3.0.2 on 2020-02-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('url', models.URLField(null=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('choice1', models.TextField(verbose_name='question1')),
                ('choice2', models.TextField(verbose_name='question2')),
                ('choice3', models.TextField(verbose_name='question3')),
                ('choice4', models.TextField(verbose_name='question4')),
                ('answer', models.CharField(max_length=10)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='own.Quiz1')),
            ],
        ),
    ]