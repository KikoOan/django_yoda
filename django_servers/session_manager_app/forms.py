from django import forms
from django.db import models
from django.forms import ModelForm

class SessionId(forms.Form):
    session_id = forms.CharField(label='Session', max_length=5)

class telescop_parameters(models.Model):

    config_id = models.CharField(max_length=10)
    frontends = models.CharField(max_length=10)
    febename = models.CharField(max_length=10)
    fecha   = models.DateField(auto_now=True)    

    def __unicode__(self):
        return self.config_id
    
    
class telescop_parameters_form (ModelForm):

    class Meta:
        model = telescop_parameters
        fields = ['config_id','frontends', 'febename']



class sb_pol(models.Model):
    pol_1 = models.BooleanField()
    pol_2 = models.BooleanField()


class sb_oscillator(models.Model):
    min = models.FloatField()
    max = models.FloatField()

class febe_parameters(models.Model):

    FEBES = [
        ('febe1', 'Febe1'),
        ('febe2', 'Febe2'),
        ('febe3', 'Febe3'),
        ('febe4', 'Febe4'),
    ]
    

    session_id = models.CharField(max_length=12)
    description = models.CharField(max_length=256)
    febe_id = models.CharField(max_length=10, choices= FEBES)
    #SB1 = models.ForeignKey(sb_pol, on_delete=models.CASCADE)
    sb1_pol1   = models.BooleanField(default=False)
    sb1_pol2   = models.BooleanField(default=False)
    sb2_pol1   = models.BooleanField(default=False)
    sb2_pol2   = models.BooleanField(default=False)
    sb3_pol1   = models.BooleanField(default=False)
    sb3_pol2   = models.BooleanField(default=False)
    sb4_pol1   = models.BooleanField(default=False)
    sb4_pol2   = models.BooleanField(default=False)
    sb5_pol1   = models.BooleanField(default=False)
    sb5_pol2   = models.BooleanField(default=False)
    sb6_pol1   = models.BooleanField(default=False)
    sb6_pol2   = models.BooleanField(default=False)
    sb7_pol1   = models.BooleanField(default=False)
    sb7_pol2   = models.BooleanField(default=False)
    sb8_pol1   = models.BooleanField(default=False)
    sb8_pol2   = models.BooleanField(default=False)
    all_sb_pol1 = models.BooleanField(default=False)
    all_sb_pol2 = models.BooleanField(default=False)
    oscillator_min = models.FloatField(default = 22.0)
    oscillator_max = models.FloatField(default = 47.0)

    #source
    source = models.CharField(max_length=12)
    offset_eq   = models.BooleanField(default=False)
    offset_hq   = models.BooleanField(default=False)
    reference   = models.FloatField(default = 0.0)


    #set-up
    aim = models.BooleanField(default=False)
    cal = models.BooleanField(default=False)
    foc = models.BooleanField(default=False)
    val_time = models.FloatField(default = 10)
    first_time = models.BooleanField(default=False)
    #integrations
    on      = models.BooleanField(default=False)
    onoff   = models.BooleanField(default=False)
    fsw     = models.BooleanField(default=False)
    skydids = models.BooleanField(default=False)
    wobbler = models.BooleanField(default=False)




    #sb_osc_1   = sb_oscillator()
    #sb_osc_2   = sb_oscillator()
    #sb_osc_3   = sb_oscillator()
    #sb_osc_4   = sb_oscillator()
    #sb_osc_5   = sb_oscillator()
    #sb_osc_6   = sb_oscillator()
    #sb_osc_7   = sb_oscillator()
    #sb_osc_8   = sb_oscillator()
    #sb_osc_all = sb_oscillator()
    #sb_osc_all = sb_oscillator()

    def __unicode__(self):
        return self.session_id


class select_all_parameters_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = "__all__"




class select_febe_parameters_id_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = ['session_id','description']







class febe_parameters_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = ['session_id','description', 'febe_id', 'all_sb_pol1', 'all_sb_pol2', 'oscillator_min', 'oscillator_max']

class select_sources_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = ['session_id','source', 'offset_eq', 'offset_hq']

class setup_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = ['session_id','aim', 'cal', 'foc', 'val_time', 'first_time']

class integration_form (ModelForm):

    class Meta:
        model = febe_parameters
        fields = ['session_id','on', 'onoff', 'fsw', 'skydids', 'wobbler']



