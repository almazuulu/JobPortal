# Generated by Django 4.2.5 on 2023-09-21 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0003_alter_jobposition_job_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('profile_image', models.ImageField(blank=True, default='photos/comments/userdef.png', null=True, upload_to='photos/users/')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('current_job_title', models.CharField(blank=True, max_length=255)),
                ('current_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('expected_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('applied_jobs', models.ManyToManyField(blank=True, related_name='applicants', to='jobs.jobposition')),
                ('favorited_jobs', models.ManyToManyField(blank=True, related_name='favorited_by', to='jobs.jobposition')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobprofiles.userprofile')),
            ],
        ),
    ]