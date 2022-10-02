# Generated by Django 3.2.15 on 2022-09-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaultPickers', '0001_initial'),
        ('bazaar', '0007_remove_productsubcategory_mrp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bazaar',
            name='dist',
        ),
        migrations.AddField(
            model_name='bazaar',
            name='district',
            field=models.ManyToManyField(to='defaultPickers.District'),
        ),
    ]
