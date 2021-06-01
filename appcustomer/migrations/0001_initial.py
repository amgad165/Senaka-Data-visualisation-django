# Generated by Django 3.2.1 on 2021-05-05 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=200, verbose_name='Customer Number')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Customer Name')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Country')),
                ('prov_state', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prov/State')),
                ('postal_zip', models.CharField(blank=True, max_length=200, null=True, verbose_name='Postal_Zip')),
                ('fst', models.CharField(blank=True, max_length=200, null=True, verbose_name='FST')),
                ('pst', models.CharField(blank=True, max_length=200, null=True, verbose_name='PST')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fax')),
                ('ship', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ship Via')),
                ('sort', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sort Name')),
                ('contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact')),
                ('terms', models.IntegerField(blank=True, null=True, verbose_name='Terms Code')),
                ('gst', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100, verbose_name='GST')),
                ('usa', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100, verbose_name='USA Account')),
                ('discount', models.FloatField(blank=True, null=True, verbose_name='Discount')),
                ('Oceanview_discount', models.FloatField(blank=True, null=True, verbose_name='Oceanview Door Discount')),
                ('vista_discount', models.FloatField(blank=True, null=True, verbose_name='Vista Door Discount')),
                ('credit', models.FloatField(blank=True, null=True, verbose_name='Credit Limit')),
                ('date_opened', models.DateField(blank=True, null=True, verbose_name='Date Opened')),
                ('mp', models.FloatField(blank=True, null=True, verbose_name='MP Lock Price')),
                ('free', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100, verbose_name='Free MP Lock')),
                ('fh', models.FloatField(blank=True, null=True, verbose_name='FH Price')),
                ('remark1', models.CharField(blank=True, max_length=200, verbose_name='Remark1')),
                ('remark2', models.CharField(blank=True, max_length=200, verbose_name='Remark2')),
                ('remark3', models.CharField(blank=True, max_length=200, verbose_name='Remark3')),
                ('remark4', models.CharField(blank=True, max_length=200, verbose_name='Remark4')),
                ('remark5', models.CharField(blank=True, max_length=200, verbose_name='Remark5')),
                ('email1', models.CharField(blank=True, max_length=200, verbose_name='Email #1')),
                ('email2', models.CharField(blank=True, max_length=200, verbose_name='Email #2')),
                ('mobile1', models.CharField(blank=True, max_length=200, verbose_name='Mobile #1')),
                ('mobile2', models.CharField(blank=True, max_length=200, verbose_name='Mobile #2')),
                ('pst_rate', models.FloatField(blank=True, null=True, verbose_name='PST Rate')),
                ('gst_rate', models.FloatField(blank=True, null=True, verbose_name='GST Rate')),
                ('hst_rate', models.FloatField(blank=True, null=True, verbose_name='HST Rate')),
                ('total_only_on_order', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100, verbose_name='Total only on order Acknoledement')),
                ('total_only_on_qutes', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100, verbose_name='Total only on Qutes')),
                ('wite', models.FloatField(blank=True, null=True, verbose_name='Wite packing charge')),
                ('color', models.FloatField(blank=True, null=True, verbose_name='Colour packing charge')),
                ('glass', models.FloatField(blank=True, null=True, verbose_name='Glass only packing charge')),
                ('outside_color', models.FloatField(blank=True, null=True, verbose_name='Outside colour #8 upcharge')),
                ('account_type', models.CharField(blank=True, choices=[('Live', 'Live'), ('Test', 'Test'), ('Both', 'Both')], max_length=200, null=True, verbose_name='Account Type')),
                ('account_representative_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Representative name')),
                ('account_representative_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Representative phone extension number')),
                ('account_representative_cell_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Representative cell phone')),
                ('account_representative_mail1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Representative email1')),
                ('account_representative_mail2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Representative email2')),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
    ]
