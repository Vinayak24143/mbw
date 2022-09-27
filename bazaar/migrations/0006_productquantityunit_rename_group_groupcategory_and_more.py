# Generated by Django 4.1.1 on 2022-09-27 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('defaultPickers', '0001_initial'),
        ('bazaar', '0005_remove_bazaar_city_remove_bazaar_dist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductQuantityUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Group',
            new_name='GroupCategory',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='groupCategory',
            field=models.ManyToManyField(to='bazaar.groupcategory'),
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='mrp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='per_unit_weight',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='productCategory',
            field=models.ManyToManyField(to='bazaar.productcategory'),
        ),
        migrations.RemoveField(
            model_name='bazaar',
            name='state',
        ),
        migrations.AddField(
            model_name='productsubcategory',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bazaar.productquantityunit'),
        ),
        migrations.AddField(
            model_name='bazaar',
            name='state',
            field=models.ManyToManyField(to='defaultPickers.state'),
        ),
    ]