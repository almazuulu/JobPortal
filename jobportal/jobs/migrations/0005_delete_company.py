# Generated by Django 4.2.5 on 2023-09-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_jobposition_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]