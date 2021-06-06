# Generated by Django 3.0.8 on 2021-06-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210606_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petition',
            name='status',
        ),
        migrations.AddField(
            model_name='agenda',
            name='status',
            field=models.CharField(blank=True, choices=[('A', 'Active'), ('X', 'End'), ('W', 'Waiting')], max_length=1, null=True, verbose_name='Status'),
        ),
    ]
