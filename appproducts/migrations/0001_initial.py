# Generated by Django 3.1.7 on 2021-04-24 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mdl_door_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_option_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Door Options',
            },
        ),
        migrations.CreateModel(
            name='mdl_glass_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glass_type_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('D_T', models.CharField(choices=[('D', 'D'), ('T', 'T')], default='D', max_length=100, verbose_name='D/T')),
                ('Price_3mm', models.FloatField(default=0.0, verbose_name='3mm Price')),
                ('Price_4mm', models.FloatField(default=0.0, verbose_name='4mm Price')),
                ('Price_5mm', models.FloatField(default=0.0, verbose_name='5mm Price')),
                ('Price_6mm', models.FloatField(default=0.0, verbose_name='6mm Price')),
                ('Price_7mm', models.FloatField(default=0.0, verbose_name='7mm Price')),
                ('Price_8mm', models.FloatField(default=0.0, verbose_name='8mm Price')),
                ('Price_9mm', models.FloatField(default=0.0, verbose_name='9mm Price')),
                ('Price_10mm', models.FloatField(default=0.0, verbose_name='10mm Price')),
                ('Price_11mm', models.FloatField(default=0.0, verbose_name='11mm Price')),
                ('Price_12mm', models.FloatField(default=0.0, verbose_name='12mm Price')),
                ('mil', models.FloatField(default=0.0, verbose_name='MIL')),
                ('ot', models.FloatField(default=0.0, verbose_name='OT')),
                ('D', models.FloatField(default=0.0, verbose_name='D')),
                ('E', models.FloatField(default=0.0, verbose_name='E')),
                ('F', models.FloatField(default=0.0, verbose_name='F')),
                ('M', models.FloatField(default=0.0, verbose_name='M')),
                ('G', models.CharField(default=0.0, max_length=200, verbose_name='G')),
                ('H', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='H [ Y/N ]')),
                ('I', models.CharField(max_length=200, verbose_name='I')),
                ('J', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='J [ Y/N ]')),
                ('K', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='K [ Y/N ]')),
            ],
            options={
                'verbose_name': 'Glass Type',
            },
        ),
        migrations.CreateModel(
            name='mdl_grill_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grill_type_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('type', models.CharField(max_length=200, verbose_name='Type')),
                ('colour', models.CharField(max_length=200, verbose_name='Colour')),
                ('matrial', models.CharField(max_length=200, verbose_name='Matrial')),
                ('sqf', models.CharField(choices=[('S', 'S'), ('F', 'F')], default='S', max_length=100, verbose_name='SQ/F')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('start_price', models.FloatField(default=0.0, verbose_name='Start Price')),
                ('min', models.FloatField(default=0.0, verbose_name='Min')),
                ('cost', models.FloatField(default=0.0, verbose_name='Cost')),
            ],
            options={
                'verbose_name': 'Grill Type',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_1',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_2',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_3',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_4',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_5',
            },
        ),
        migrations.CreateModel(
            name='mdl_miscellaneous_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miscellaneous_id', models.IntegerField(verbose_name='MISC #')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('um', models.CharField(max_length=200, verbose_name='U/M')),
                ('discounttable', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='Discounttable')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Miscellaneous_6',
            },
        ),
        migrations.CreateModel(
            name='mdl_part_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multipoint_lock', models.FloatField(default=0.0, verbose_name='Multipoint Lock')),
                ('folding_handle', models.FloatField(default=0.0, verbose_name='Folding Handle')),
                ('casement_over_max_width', models.FloatField(default=0.0, verbose_name='Casement over Max Width')),
                ('su_shape_charge', models.FloatField(default=0.0, verbose_name='SU Shape charge')),
                ('multipoint_lock_option_2', models.FloatField(default=0.0, verbose_name='Multipoint Lock Option 2')),
                ('multipoint_lock_option_3', models.FloatField(default=0.0, verbose_name='Multipoint Lock Option 3')),
                ('single_hung_shape_charge', models.FloatField(default=0.0, verbose_name='Single Hung Shape Charge')),
                ('bay_coupler_charge', models.FloatField(default=0.0, verbose_name='Bay Coupler Charge')),
                ('extra_brickmould_bay_charge', models.FloatField(default=0.0, verbose_name='Extra Brickmould Bay Charge')),
                ('extra_jamb_ext_bay_charge', models.FloatField(default=0.0, verbose_name='Extra Jamb Ext Bay Charge')),
                ('plywood_int_finish_bay_charge', models.FloatField(default=0.0, verbose_name='plywood Int Finish Bay Charge')),
                ('inches_to_subt_from_ht_if_plywood_int_finish', models.FloatField(default=0.0, verbose_name='Inches to Subt from HT if plywood Int Finish')),
            ],
            options={
                'verbose_name': 'Part Price',
            },
        ),
        migrations.CreateModel(
            name='mdl_rosettes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rosettes_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Rosettes',
            },
        ),
        migrations.CreateModel(
            name='mdl_spacer_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spacer_type_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(default=0.0, verbose_name='Price per Lin FT')),
                ('add_on', models.FloatField(default=0.0, verbose_name='Add on')),
            ],
            options={
                'verbose_name': 'Spacer Type',
            },
        ),
        migrations.CreateModel(
            name='mdl_window_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField(blank=True, null=True, verbose_name='ITEM NUMBER')),
                ('item_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='ITEM DSCRIPTION')),
                ('label_multiplier', models.IntegerField(blank=True, null=True, verbose_name='LABEL MULTIPLIER')),
                ('item_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='ITEM TYPE')),
                ('group_number', models.IntegerField(blank=True, null=True, verbose_name='GROUP NUMBER')),
                ('inside_color', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, null=True, verbose_name='INSIDE_COLOR')),
                ('painted_price_outside', models.FloatField(blank=True, default=0.0, null=True, verbose_name='PAINTED PRICE(OUTSIDE)')),
                ('painted_price_inside', models.FloatField(blank=True, default=0.0, null=True, verbose_name='PAINTED PRICE(INSIDE)')),
                ('stain_price_outside', models.FloatField(blank=True, default=0.0, null=True, verbose_name='STAIN PRICE(OUTSIDE)')),
                ('stain_price_inside', models.FloatField(blank=True, default=0.0, null=True, verbose_name='STAIN PRICE(INSIDE)')),
                ('urban_output', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, null=True, verbose_name='URBAN OUTPUT')),
                ('urban_material', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN MATERIAL')),
                ('urban_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN MODEL')),
                ('urban_part', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN PART')),
                ('urban_code_digit', models.IntegerField(blank=True, null=True, verbose_name='LABEL MULTIPLIER')),
                ('urban_of_bins', models.IntegerField(blank=True, null=True, verbose_name='URBAN OF BINS')),
                ('urban_csv_file_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN CSV FILE NAME')),
                ('urban_width_label', models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], default=0, null=True, verbose_name='URBAN WITH LABEL')),
                ('urban_ht_label', models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], default=0, null=True, verbose_name='URBAN HT LABEL')),
                ('urban_item_size_for_barcode', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], max_length=200, null=True, verbose_name='URBAN ITEM SIZE FOR BARCODE')),
                ('tiger_stop_output', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, null=True, verbose_name='TIGER STOP OUTPUT')),
                ('tiger_stop_material', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIGER STOP MATERIAL')),
                ('tiger_stop_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIGER STOP MODEL')),
                ('tiger_stop_part', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIGER STOP PART')),
                ('tiger_stop_code_digit', models.IntegerField(blank=True, null=True, verbose_name='TIGER STOP CODE DIGIT')),
                ('tiger_of_bins', models.IntegerField(blank=True, null=True, verbose_name='TIGER STOP OF BINS')),
                ('tiger_stop_csv_file_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIGER STOP CSV FILE NAME')),
                ('tiger_width_label', models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], default=0, null=True, verbose_name='TIGER STOP WITH LABEL')),
                ('tiger_ht_label', models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], default=0, null=True, verbose_name='TIGER STOP HT LABEL')),
                ('tiger_item_size_for_barcode', models.IntegerField(blank=True, null=True, verbose_name='TIGER STOP ITEM SIZE FOR BARCODE')),
            ],
            options={
                'verbose_name': 'Window Item',
            },
        ),
        migrations.CreateModel(
            name='mdl_window_option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window_option_id', models.IntegerField(verbose_name='NO')),
                ('shot_code', models.CharField(max_length=10, verbose_name='Short Code')),
                ('type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Type')),
                ('sm_casing', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Sm Casing')),
                ('lg_casing', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Lg Casing')),
                ('painted_inside', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Painted Inside')),
                ('painted_outside', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Painted Outside')),
                ('rosette', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Rosette')),
                ('xtra', models.IntegerField(default=0, verbose_name='Xtra')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('mat_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mat Code')),
                ('pricing_width', models.FloatField(default=0.0, verbose_name='Pricing Width')),
                ('width_qty', models.FloatField(default=0.0, verbose_name='Width Qty')),
                ('pricing_ht', models.FloatField(default=0.0, verbose_name='Pricing Ht')),
                ('ht_qty', models.FloatField(default=0.0, verbose_name='Ht Qty')),
                ('stained', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Stained')),
                ('white_price', models.FloatField(verbose_name='White Price')),
                ('colour_price', models.FloatField(verbose_name='Colour Price')),
                ('stain_price', models.FloatField(default=0.0, verbose_name='Stain Price')),
                ('l_f_s', models.CharField(choices=[('L', 'L'), ('F', 'F'), ('S', 'S')], default='L', max_length=100, verbose_name='Lin/Fix/Sq')),
                ('cutting_width', models.FloatField(default=0.0, verbose_name='Cutting Width')),
                ('cutting_ht', models.FloatField(default=0.0, verbose_name='Cutting Ht')),
                ('size_Width', models.FloatField(default=0.0, verbose_name='BM Size Width')),
                ('size_ht', models.FloatField(default=0.0, verbose_name='BM Size Ht')),
                ('urban', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=100, verbose_name='URBAN')),
                ('urban_material', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN Material')),
                ('urban_model', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN Model')),
                ('urban_part', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN Part')),
                ('urban_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='URBAN Code')),
                ('urban_folder', models.CharField(blank=True, choices=[('Y', 'Y'), ('N', 'N')], default='', max_length=100, null=True, verbose_name='2nd URBAN Folder')),
                ('bins', models.IntegerField(verbose_name='Bins')),
                ('outs_painted_price', models.FloatField(default=0.0, verbose_name='Outs Painted Price')),
                ('inside_painted_price', models.FloatField(default=0.0, verbose_name='Inside Painted Price')),
                ('outs_stain_price', models.FloatField(default=0.0, verbose_name='Out Stain Price')),
                ('inside_stain_price', models.FloatField(default=0.0, verbose_name='Inside Stain Price')),
            ],
            options={
                'verbose_name': 'Window Options',
            },
        ),
        migrations.CreateModel(
            name='mdl_window_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Window Type')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('folding_handle', models.CharField(choices=[('Y', 'Y'), ('N', 'N'), ('O', 'O')], default='Y', max_length=100, verbose_name='Folding Handle (Y/N/O)')),
                ('multipt_lock', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Multipt Lock')),
                ('group_code', models.IntegerField(verbose_name='Group Code (1-20)')),
                ('style_code', models.IntegerField(verbose_name='Style Code')),
                ('price_code', models.CharField(max_length=200, verbose_name='Price Code')),
                ('sealed_unit', models.FloatField(default=0.0, verbose_name='OT of Sealed Unit')),
                ('output_urban', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Output to Urban Y/N')),
                ('inactive', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=100, verbose_name='Inactive Y/N')),
                ('inside_stain_price', models.FloatField(default=0.0, verbose_name='Inside Stain Price')),
                ('outside_stain_price', models.FloatField(default=0.0, verbose_name='Outside Stain Price')),
                ('inside_stain_price_over', models.FloatField(default=0.0, verbose_name='Inside Stain Price Over 14SF')),
                ('outside_stain_price_over', models.FloatField(default=0.0, verbose_name='Outside Stain Price Over 14SF')),
                ('extra_price', models.FloatField(default=0.0, verbose_name='Extra Price,Triple or Over 10SF')),
            ],
            options={
                'verbose_name': 'Window Type',
            },
        ),
        migrations.CreateModel(
            name='mdl_window_maxmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum_width_double', models.FloatField(default=0.0, verbose_name='Maximum Width Double')),
                ('minimum_width_double', models.FloatField(default=0.0, verbose_name='Minimum Width Double')),
                ('maximum_width_triple', models.FloatField(default=0.0, verbose_name='Maximum Width Triple')),
                ('minimum_width_triple', models.FloatField(default=0.0, verbose_name='Minimum Width Triple')),
                ('maximum_width_quadruple', models.FloatField(default=0.0, verbose_name='Maximum Width Quadruple')),
                ('minimum_width_quadruple', models.FloatField(default=0.0, verbose_name='Minimum Width Quadruple')),
                ('maximum_height_double', models.FloatField(default=0.0, verbose_name='Maximum Height Double')),
                ('minimum_height_double', models.FloatField(default=0.0, verbose_name='Minimum Height Double')),
                ('maximun_height_triple', models.FloatField(default=0.0, verbose_name='Maximum Height Triple')),
                ('minimun_height_triple', models.FloatField(default=0.0, verbose_name='Minimum Height Triple')),
                ('maximun_height_quadruple', models.FloatField(default=0.0, verbose_name='Maximum Height Quadruple')),
                ('minimun_height_quadruple', models.FloatField(default=0.0, verbose_name='Minimum Height Quadruple')),
                ('maximum_sq_ft_double', models.FloatField(default=0.0, verbose_name='Maximum Sq Ft Double')),
                ('minimum_sq_ft_double', models.FloatField(default=0.0, verbose_name='Minimum Sq Ft Double')),
                ('maximum_sq_ft_triple', models.FloatField(default=0.0, verbose_name='Maximum Sq Ft Triple')),
                ('minimum_sq_ft_triple', models.FloatField(default=0.0, verbose_name='Minimum Sq Ft Triple')),
                ('maximum_sq_ft_quadruple', models.FloatField(default=0.0, verbose_name='Maximum Sq Ft Quadruple')),
                ('minimum_sq_ft_quadruple', models.FloatField(default=0.0, verbose_name='Minimum Sq Ft Quadruple')),
                ('window_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appproducts.mdl_window_type', verbose_name='Window Type')),
            ],
            options={
                'verbose_name': 'Window Max/Min',
            },
        ),
        migrations.CreateModel(
            name='mdl_patio_door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patio_door_id', models.IntegerField(verbose_name='NO')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('stock', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Yes', max_length=100, verbose_name='Stock')),
                ('qty', models.FloatField(default=0.0, verbose_name='Qty On Hand')),
                ('manufacturer', models.CharField(max_length=200, verbose_name='Manufacturer')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appproducts.mdl_door_option', verbose_name='Door Options')),
            ],
            options={
                'verbose_name': 'Patio Door',
            },
        ),
        migrations.CreateModel(
            name='mdl_deductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ln', models.CharField(max_length=200, verbose_name='LN')),
                ('it', models.IntegerField(verbose_name='IT')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Item Name')),
                ('qty', models.FloatField(default=0.0, verbose_name='QTY')),
                ('xy0', models.FloatField(default=0.0, verbose_name='X0/Y0')),
                ('xy1', models.FloatField(default=0.0, verbose_name='X1/Y1')),
                ('xy2', models.FloatField(default=0.0, verbose_name='X2/Y2')),
                ('xy3', models.FloatField(default=0.0, verbose_name='X3/Y3')),
                ('xy4', models.FloatField(default=0.0, verbose_name='X4/Y4')),
                ('window_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appproducts.mdl_window_type', verbose_name='Window Type')),
            ],
            options={
                'verbose_name': 'Window Deduction',
            },
        ),
        migrations.CreateModel(
            name='mdl_color_price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_code', models.IntegerField(verbose_name='Price Code')),
                ('sq_ft', models.FloatField(default=0.0, verbose_name='SQ FT')),
                ('white_swd', models.FloatField(default=0.0, verbose_name='White SWD')),
                ('cream_1', models.FloatField(default=0.0, verbose_name='Cream -1')),
                ('cream_2', models.FloatField(default=0.0, verbose_name='Cream -2')),
                ('brown', models.FloatField(default=0.0, verbose_name='Brown')),
                ('swd', models.FloatField(default=0.0, verbose_name='SWD')),
                ('pebble', models.FloatField(default=0.0, verbose_name='Pebble')),
                ('c_brown', models.FloatField(default=0.0, verbose_name='C.Brown')),
                ('window_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appproducts.mdl_window_type', verbose_name='Window Type')),
            ],
            options={
                'verbose_name': 'Color Price',
            },
        ),
    ]