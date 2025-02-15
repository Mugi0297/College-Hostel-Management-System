# Generated by Django 5.1.2 on 2024-10-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_rename_date_submitted_grievance_date_reported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='evening_attendance',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='morning_attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='time_slot',
            field=models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='Absent', max_length=10),
            preserve_default=False,
        ),
    ]
