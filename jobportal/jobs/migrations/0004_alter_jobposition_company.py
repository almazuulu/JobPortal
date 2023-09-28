# Generated by Django 4.2.5 on 2023-09-26 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobprofiles', '0002_companyprofile'),
        ('jobs', '0003_alter_jobposition_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobprofiles.companyprofile'),
        ),
    ]