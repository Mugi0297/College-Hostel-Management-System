# Generated by Django 5.1.2 on 2024-10-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_remove_attendance_evening_attendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=10),
        ),
    ]
