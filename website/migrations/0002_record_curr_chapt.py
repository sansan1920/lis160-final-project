# Generated by Django 5.1.4 on 2024-12-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='curr_chapt',
            field=models.CharField(max_length=20, null=True),
        ),
    ]