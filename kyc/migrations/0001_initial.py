# Generated by Django 4.1.1 on 2022-10-03 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kyc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KYCDocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KYCDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=254, upload_to=kyc.models.kycDocumentImage)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kyc.kycdocumenttype')),
            ],
        ),
        migrations.CreateModel(
            name='KYCApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending')),
                ('rejection_reason', models.TextField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kyc.kycdocument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kycApplication', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
