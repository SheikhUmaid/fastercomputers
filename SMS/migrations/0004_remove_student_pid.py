# Generated by Django 3.2.13 on 2022-07-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_student_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pid',
        ),
    ]
