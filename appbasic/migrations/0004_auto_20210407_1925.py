# Generated by Django 3.1.7 on 2021-04-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbasic', '0003_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting'},
        ),
        migrations.AlterField(
            model_name='settings',
            name='VP_receiving',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='cutting',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='pnt_receiving',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='shipping',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='weld_clean',
            field=models.IntegerField(),
        ),
    ]
