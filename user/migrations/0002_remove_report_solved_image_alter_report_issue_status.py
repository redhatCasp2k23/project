# Generated by Django 4.2 on 2023-04-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='solved_image',
        ),
        migrations.AlterField(
            model_name='report',
            name='issue_status',
            field=models.CharField(choices=[('0', 'pending'), ('1', 'solved'), ('2', 'closeCase'), ('3', 'rejected')], default='0', max_length=1, verbose_name='issue_status'),
        ),
    ]
