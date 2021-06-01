from django.db import models

# Create your models here.
y_n_select=(("Y","Y"),("N","N"))
l_f_s_select=(("L","L"),("F","F"),("S","S"))
s_f_select=(("S","S"),("F","F"))
y_n_o_select=(("Y","Y"),("N","N"),("O","O"))
d_t_select=(("D","D"),("T","T"))
zero_one_select=((0,0),(1,1))

class mdl_door_option(models.Model):
    door_option_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price")
    class Meta:
        verbose_name=u"Door Options"
    def __str__(self):
        return "%s" % (self.door_option_id)

class mdl_patio_door(models.Model):
    patio_door_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price")
    stock=models.CharField(choices=y_n_select,default="Yes",verbose_name="Stock",max_length=100)
    qty=models.FloatField(verbose_name="Qty On Hand",default=0.00)
    manufacturer=models.CharField(verbose_name="Manufacturer",max_length=200)
    option=models.ForeignKey(mdl_door_option,verbose_name="Door Options",null=True,blank=True,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name=u"Patio Door"
    def __str__(self):
        return "%s" % (self.patio_door_id)

class mdl_window_option(models.Model):
    window_option_id=models.IntegerField(verbose_name="NO")
    shot_code=models.CharField(verbose_name="Short Code",max_length=10)
    type=models.CharField(verbose_name="Type",max_length=10,null=True,blank=True)
    sm_casing=models.CharField(choices=y_n_select,default="Y",verbose_name="Sm Casing",max_length=100)
    lg_casing=models.CharField(choices=y_n_select,default="Y",verbose_name="Lg Casing",max_length=100)
    painted_inside=models.CharField(choices=y_n_select,default="Y",verbose_name="Painted Inside",max_length=100)
    painted_outside=models.CharField(choices=y_n_select,default="Y",verbose_name="Painted Outside",max_length=100)
    rosette=models.CharField(choices=y_n_select,default="Y",verbose_name="Rosette",max_length=100)
    xtra=models.IntegerField(verbose_name="Xtra",default=0)
    description=models.CharField(verbose_name="Description",max_length=200)
    mat_code=models.CharField(verbose_name="Mat Code",max_length=200,null=True,blank=True)
    pricing_width=models.FloatField(verbose_name="Pricing Width",default=0.00)
    width_qty=models.FloatField(verbose_name="Width Qty",default=0.00)
    pricing_ht=models.FloatField(verbose_name="Pricing Ht",default=0.00)
    ht_qty=models.FloatField(verbose_name="Ht Qty",default=0.00)
    stained =models.CharField(choices=y_n_select,default="Y",verbose_name="Stained",max_length=100)
    white_price=models.FloatField(verbose_name="White Price")
    colour_price=models.FloatField(verbose_name="Colour Price")
    stain_price=models.FloatField(verbose_name="Stain Price",default=0.00)
    l_f_s=models.CharField(choices=l_f_s_select,default="L",verbose_name="Lin/Fix/Sq",max_length=100)
    cutting_width=models.FloatField(verbose_name="Cutting Width",default=0.00)
    cutting_ht=models.FloatField(verbose_name="Cutting Ht",default=0.00)
    size_Width=models.FloatField(verbose_name="BM Size Width",default=0.00)
    size_ht=models.FloatField(verbose_name="BM Size Ht",default=0.00)
    urban=models.CharField(choices=y_n_select,default="N",verbose_name="URBAN",max_length=100)
    urban_material=models.CharField(verbose_name="URBAN Material",max_length=200,null=True,blank=True)
    urban_model=models.CharField(verbose_name="URBAN Model",max_length=200,null=True,blank=True)
    urban_part=models.CharField(verbose_name="URBAN Part",max_length=200,null=True,blank=True)
    urban_code=models.CharField(verbose_name="URBAN Code",max_length=200,null=True,blank=True)
    urban_folder=models.CharField(choices=y_n_select,null=True,blank=True,default="",verbose_name="2nd URBAN Folder",max_length=100)
    bins=models.IntegerField(verbose_name="Bins")
    outs_painted_price=models.FloatField(verbose_name="Outs Painted Price",default=0.00)
    inside_painted_price=models.FloatField(verbose_name="Inside Painted Price",default=0.00)
    outs_stain_price=models.FloatField(verbose_name="Out Stain Price",default=0.00)
    inside_stain_price=models.FloatField(verbose_name="Inside Stain Price",default=0.00)
    class Meta:
        verbose_name=u"Window Options"
    def __str__(self):
        return "%s" % (self.window_option_id)

class mdl_spacer_type(models.Model):
    spacer_type_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price per Lin FT",default=0.00)
    add_on=models.FloatField(verbose_name="Add on",default=0.00)
    class Meta:
        verbose_name=u"Spacer Type"
    def __str__(self):
        return "%s" % (self.spacer_type_id)

class mdl_rosettes(models.Model):
    rosettes_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    class Meta:
        verbose_name=u"Rosettes"
    def __str__(self):
        return "%s" % (self.rosettes_id)

class mdl_grill_type(models.Model):
    grill_type_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    type=models.CharField(verbose_name="Type",max_length=200)
    colour=models.CharField(verbose_name="Colour",max_length=200)
    matrial=models.CharField(verbose_name="Matrial",max_length=200)
    sqf=models.CharField(choices=s_f_select,default="S",verbose_name="SQ/F",max_length=100)
    price=models.FloatField(verbose_name="Price",default=0.00)
    start_price=models.FloatField(verbose_name="Start Price",default=0.00)
    min=models.FloatField(verbose_name="Min",default=0.00)
    cost=models.FloatField(verbose_name="Cost",default=0.00)
    class Meta:
        verbose_name=u"Grill Type"
    def __str__(self):
        return "%s" % (self.grill_type_id)

class mdl_window_type(models.Model):
    name=models.CharField(verbose_name="Window Type",max_length=200)
    description = models.CharField(verbose_name="Description",max_length=200)
    folding_handle=models.CharField(choices=y_n_o_select,default="Y",verbose_name="Folding Handle (Y/N/O)",max_length=100)
    multipt_lock=models.CharField(choices=y_n_select,default="Y",verbose_name="Multipt Lock",max_length=100)
    group_code=models.IntegerField(verbose_name="Group Code (1-20)")
    style_code=models.IntegerField(verbose_name="Style Code")
    price_code=models.CharField(verbose_name="Price Code",max_length=200)
    sealed_unit=models.FloatField(verbose_name="OT of Sealed Unit",default=0.00)
    output_urban=models.CharField(choices=y_n_select,default="Y",verbose_name="Output to Urban Y/N",max_length=100)
    inactive=models.CharField(choices=y_n_select,default="Y",verbose_name="Inactive Y/N",max_length=100)
    inside_stain_price=models.FloatField(verbose_name="Inside Stain Price",default=0.00)
    outside_stain_price=models.FloatField(verbose_name="Outside Stain Price",default=0.00)
    inside_stain_price_over=models.FloatField(verbose_name="Inside Stain Price Over 14SF",default=0.00)
    outside_stain_price_over=models.FloatField(verbose_name="Outside Stain Price Over 14SF",default=0.00)
    extra_price=models.FloatField(verbose_name="Extra Price,Triple or Over 10SF",default=0.00)
    class Meta:
        verbose_name=u"Window Type"
    def __str__(self):
        return "%s" % (self.name)

class mdl_window_maxmin(models.Model):
    window_type=models.ForeignKey(mdl_window_type,verbose_name="Window Type",null=True,blank=True,on_delete=models.DO_NOTHING)
    maximum_width_double=models.FloatField(verbose_name="Maximum Width Double",default=0.00)
    minimum_width_double=models.FloatField(verbose_name="Minimum Width Double",default=0.00)
    maximum_width_triple=models.FloatField(verbose_name="Maximum Width Triple",default=0.00)
    minimum_width_triple=models.FloatField(verbose_name="Minimum Width Triple",default=0.00)
    maximum_width_quadruple=models.FloatField(verbose_name="Maximum Width Quadruple",default=0.00)
    minimum_width_quadruple=models.FloatField(verbose_name="Minimum Width Quadruple",default=0.00)
    maximum_height_double=models.FloatField(verbose_name="Maximum Height Double",default=0.00)
    minimum_height_double=models.FloatField(verbose_name="Minimum Height Double",default=0.00)
    maximun_height_triple=models.FloatField(verbose_name="Maximum Height Triple",default=0.00)
    minimun_height_triple=models.FloatField(verbose_name="Minimum Height Triple",default=0.00)
    maximun_height_quadruple=models.FloatField(verbose_name="Maximum Height Quadruple",default=0.00)
    minimun_height_quadruple=models.FloatField(verbose_name="Minimum Height Quadruple",default=0.00)
    maximum_sq_ft_double=models.FloatField(verbose_name="Maximum Sq Ft Double",default=0.00)
    minimum_sq_ft_double=models.FloatField(verbose_name="Minimum Sq Ft Double",default=0.00)
    maximum_sq_ft_triple=models.FloatField(verbose_name="Maximum Sq Ft Triple",default=0.00)
    minimum_sq_ft_triple=models.FloatField(verbose_name="Minimum Sq Ft Triple",default=0.00)
    maximum_sq_ft_quadruple=models.FloatField(verbose_name="Maximum Sq Ft Quadruple",default=0.00)
    minimum_sq_ft_quadruple=models.FloatField(verbose_name="Minimum Sq Ft Quadruple",default=0.00)
    class Meta:
        verbose_name=u"Window Max/Min"
    def __str__(self):
        return "%s" % (self.window_type)

class mdl_deductions(models.Model):
    window_type=models.ForeignKey(mdl_window_type,verbose_name="Window Type",null=True,blank=True,on_delete=models.DO_NOTHING)
    ln=models.CharField(verbose_name="LN",max_length=200)
    it=models.IntegerField(verbose_name="IT")
    name=models.CharField(verbose_name="Item Name",max_length=200,null=True,blank=True)
    qty=models.FloatField(verbose_name="QTY",default=0.00)
    xy0=models.FloatField(verbose_name="X0/Y0",default=0.00)
    xy1=models.FloatField(verbose_name="X1/Y1",default=0.00)
    xy2=models.FloatField(verbose_name="X2/Y2",default=0.00)
    xy3=models.FloatField(verbose_name="X3/Y3",default=0.00)
    xy4=models.FloatField(verbose_name="X4/Y4",default=0.00)
    class Meta:
        verbose_name=u"Window Deduction"
    def __str__(self):
        return "%s_%s_%s" % (self.ln,self.it,self.window_type)

class mdl_glass_type(models.Model):
    glass_type_id=models.IntegerField(verbose_name="NO")
    description=models.CharField(verbose_name="Description",max_length=200)
    D_T=models.CharField(choices=d_t_select,default="D",verbose_name="D/T",max_length=100)
    Price_3mm=models.FloatField(verbose_name="3mm Price",default=0.00)
    Price_4mm=models.FloatField(verbose_name="4mm Price",default=0.00)
    Price_5mm=models.FloatField(verbose_name="5mm Price",default=0.00)
    Price_6mm=models.FloatField(verbose_name="6mm Price",default=0.00)
    Price_7mm=models.FloatField(verbose_name="7mm Price",default=0.00)
    Price_8mm=models.FloatField(verbose_name="8mm Price",default=0.00)
    Price_9mm=models.FloatField(verbose_name="9mm Price",default=0.00)
    Price_10mm=models.FloatField(verbose_name="10mm Price",default=0.00)
    Price_11mm=models.FloatField(verbose_name="11mm Price",default=0.00)
    Price_12mm=models.FloatField(verbose_name="12mm Price",default=0.00)
    mil=models.FloatField(verbose_name="MIL",default=0.00)
    ot=models.FloatField(verbose_name="OT",default=0.00)
    D=models.FloatField(verbose_name="D",default=0.00)
    E=models.FloatField(verbose_name="E",default=0.00)
    F=models.FloatField(verbose_name="F",default=0.00)
    M=models.FloatField(verbose_name="M",default=0.00)
    G=models.CharField(verbose_name="G",max_length=200,default=0.00)
    H=models.CharField(choices=y_n_select,default="Y",verbose_name="H [ Y/N ]",max_length=100)
    I=models.CharField(verbose_name="I",max_length=200)
    J=models.CharField(choices=y_n_select,default="Y",verbose_name="J [ Y/N ]",max_length=100)
    K=models.CharField(choices=y_n_select,default="Y",verbose_name="K [ Y/N ]",max_length=100)
    class Meta:
        verbose_name=u"Glass Type"
    def __str__(self):
        return "%s" % (self.glass_type_id)

class mdl_miscellaneous_1(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_1"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_miscellaneous_2(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_2"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_miscellaneous_3(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_3"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_miscellaneous_4(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_4"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_miscellaneous_5(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_5"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_miscellaneous_6(models.Model):
    miscellaneous_id=models.IntegerField(verbose_name="MISC #")
    description=models.CharField(verbose_name="Description",max_length=200)
    price=models.FloatField(verbose_name="Price",default=0.00)
    um=models.CharField(verbose_name="U/M",max_length=200)
    discounttable=models.CharField(choices=y_n_select,default="N",verbose_name="Discounttable",max_length=100)
    code=models.CharField(verbose_name="Code",max_length=200,null=True,blank=True)
    class Meta:
        verbose_name=u"Miscellaneous_6"
    def __str__(self):
        return "%s" % (self.miscellaneous_id)

class mdl_color_price(models.Model):
    window_type=models.ForeignKey(mdl_window_type,verbose_name="Window Type",null=True,blank=True,on_delete=models.DO_NOTHING)
    price_code=models.IntegerField(verbose_name="Price Code")
    sq_ft=models.FloatField(verbose_name="SQ FT",default=0.00)
    white_swd=models.FloatField(verbose_name="White SWD",default=0.00)
    cream_1=models.FloatField(verbose_name="Cream -1",default=0.00)
    cream_2=models.FloatField(verbose_name="Cream -2",default=0.00)
    brown=models.FloatField(verbose_name="Brown",default=0.00)
    swd=models.FloatField(verbose_name="SWD",default=0.00)
    pebble=models.FloatField(verbose_name="Pebble",default=0.00)
    c_brown=models.FloatField(verbose_name="C.Brown",default=0.00)
    class Meta:
        verbose_name=u"Color Price"
    def __str__(self):
        return "%s" % (self.window_type)

class mdl_part_price(models.Model):
    multipoint_lock=models.FloatField (verbose_name="Multipoint Lock",default=0.00)
    folding_handle=models.FloatField(verbose_name="Folding Handle",default=0.00)
    casement_over_max_width=models.FloatField(verbose_name="Casement over Max Width",default=0.00)
    su_shape_charge=models.FloatField(verbose_name="SU Shape charge",default=0.00)
    multipoint_lock_option_2=models.FloatField(verbose_name="Multipoint Lock Option 2",default=0.00)
    multipoint_lock_option_3=models.FloatField(verbose_name="Multipoint Lock Option 3",default=0.00)
    single_hung_shape_charge=models.FloatField(verbose_name="Single Hung Shape Charge",default=0.00)
    bay_coupler_charge=models.FloatField(verbose_name="Bay Coupler Charge",default=0.00)
    extra_brickmould_bay_charge=models.FloatField(verbose_name="Extra Brickmould Bay Charge",default=0.00)
    extra_jamb_ext_bay_charge=models.FloatField(verbose_name="Extra Jamb Ext Bay Charge",default=0.00)
    plywood_int_finish_bay_charge=models.FloatField(verbose_name="plywood Int Finish Bay Charge",default=0.00)
    inches_to_subt_from_ht_if_plywood_int_finish=models.FloatField(verbose_name="Inches to Subt from HT if plywood Int Finish",default=0.00)
    class Meta:
        verbose_name=u"Part Price"
    def __str__(self):
        return "%s" % (self.multipoint_lock)

class mdl_window_item(models.Model):
    item_number=models.IntegerField(verbose_name="ITEM NUMBER", null=True, blank=True)
    item_description=models.CharField(verbose_name="ITEM DSCRIPTION",max_length=200, null=True, blank=True)
    label_multiplier=models.IntegerField(verbose_name="LABEL MULTIPLIER", null=True, blank=True)
    item_type=models.CharField(verbose_name="ITEM TYPE",max_length=200, null=True, blank=True)
    group_number=models.IntegerField(verbose_name="GROUP NUMBER", null=True, blank=True)
    inside_color=models.CharField(choices=y_n_select,default="Y",verbose_name="INSIDE_COLOR",max_length=100, null=True, blank=True)
    painted_price_outside=models.FloatField(verbose_name="PAINTED PRICE(OUTSIDE)",default=0.00, null=True, blank=True)
    painted_price_inside=models.FloatField(verbose_name="PAINTED PRICE(INSIDE)",default=0.00, null=True, blank=True)
    stain_price_outside=models.FloatField(verbose_name="STAIN PRICE(OUTSIDE)",default=0.00, null=True, blank=True)
    stain_price_inside=models.FloatField(verbose_name="STAIN PRICE(INSIDE)",default=0.00, null=True, blank=True)
    urban_output=models.CharField(choices=y_n_select,default="Y",verbose_name="URBAN OUTPUT",max_length=100, null=True, blank=True)
    urban_material=models.CharField(verbose_name="URBAN MATERIAL",max_length=200, null=True, blank=True)
    urban_model=models.CharField(verbose_name="URBAN MODEL",max_length=200, null=True, blank=True)
    urban_part=models.CharField(verbose_name="URBAN PART",max_length=200, null=True, blank=True)
    urban_code_digit=models.IntegerField(verbose_name="LABEL MULTIPLIER", null=True, blank=True)
    urban_of_bins=models.IntegerField(verbose_name="URBAN OF BINS", null=True, blank=True)
    urban_csv_file_name=models.CharField(verbose_name="URBAN CSV FILE NAME",max_length=200, null=True, blank=True)
    urban_width_label=models.IntegerField(choices=zero_one_select,default=0,verbose_name="URBAN WITH LABEL", null=True, blank=True)
    urban_ht_label=models.IntegerField(choices=zero_one_select,default=0,verbose_name="URBAN HT LABEL", null=True, blank=True)
    urban_item_size_for_barcode=models.CharField(choices=y_n_select,verbose_name="URBAN ITEM SIZE FOR BARCODE ", max_length=150,null=True, blank=True)
    tiger_stop_output=models.CharField(choices=y_n_select,default="Y",verbose_name="TIGER STOP OUTPUT",max_length=100, null=True, blank=True)
    tiger_stop_material=models.CharField(verbose_name="TIGER STOP MATERIAL",max_length=150, null=True, blank=True)
    tiger_stop_model=models.CharField(verbose_name="TIGER STOP MODEL",max_length=200, null=True, blank=True)
    tiger_stop_part=models.CharField(verbose_name="TIGER STOP PART",max_length=250, null=True, blank=True)
    tiger_stop_code_digit=models.IntegerField(verbose_name="TIGER STOP CODE DIGIT", null=True, blank=True)
    tiger_of_bins=models.IntegerField(verbose_name="TIGER STOP OF BINS", null=True, blank=True)
    tiger_stop_csv_file_name=models.CharField(verbose_name="TIGER STOP CSV FILE NAME",max_length=200, null=True, blank=True)
    tiger_width_label=models.IntegerField(choices=zero_one_select,default=0,verbose_name="TIGER STOP WITH LABEL",null=True, blank=True)
    tiger_ht_label=models.IntegerField(choices=zero_one_select,default=0,verbose_name="TIGER STOP HT LABEL",null=True, blank=True)
    tiger_item_size_for_barcode=models.IntegerField(verbose_name="TIGER STOP ITEM SIZE FOR BARCODE", null=True, blank=True)
    class Meta:
        verbose_name=u"Window Item"
    def __str__(self):
        return "%s" % (self.item_number)
