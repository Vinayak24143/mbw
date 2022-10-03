# Generated by Django 4.1.1 on 2022-10-03 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0010_rename_groups_bazaar_groupscategoties'),
        ('defaultPickers', '0001_initial'),
        ('account', '0002_remove_user_profile_user_allocatedcities_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='allocatedCities',
        ),
        migrations.RemoveField(
            model_name='user',
            name='allocatedDistricts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='allocatedStates',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bazaars',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('admin', 'admin'), ('agent', 'agent'), ('customer', 'customer')], default='admin', max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bazaars', models.ManyToManyField(blank=True, to='bazaar.bazaar')),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customertype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentType', models.CharField(choices=[('individual', 'individual'), ('agency', 'agency'), ('salesman', 'salesman')], default='individual', max_length=30)),
                ('allocatedCities', models.ManyToManyField(blank=True, related_name='allocatedCities', to='defaultPickers.city')),
                ('allocatedDistricts', models.ManyToManyField(blank=True, related_name='allocatedDistricts', to='defaultPickers.district')),
                ('allocatedStates', models.ManyToManyField(blank=True, related_name='allocatedStates', to='defaultPickers.state')),
                ('bazaars', models.ManyToManyField(blank=True, to='bazaar.bazaar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agentProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
