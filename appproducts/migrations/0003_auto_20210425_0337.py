# Generated by Django 3.1.7 on 2021-04-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appproducts', '0002_auto_20210424_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mdl_window_item',
            name='urban_item_size_for_barcode',
            field=models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], max_length=150, null=True, verbose_name='URBAN ITEM SIZE FOR BARCODE '),
        ),
    ]
