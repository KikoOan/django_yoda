from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Session(models.Model):

    session_name = models.CharField(max_length=10)
    description = models.CharField(max_length=256)
    fecha   = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.session_name
    


class Febes(models.Model):

    febe_name = models.CharField(max_length=10, unique=True)
    num_pol = models.IntegerField(validators=[MinValueValidator (limit_value=1), MaxValueValidator(limit_value=4)])
    num_sb  = models.IntegerField(validators=[MinValueValidator (limit_value=1), MaxValueValidator(limit_value=8)])
    min_lo  = models.FloatField(validators=[MinValueValidator (limit_value=8.0), MaxValueValidator(limit_value=110.0)]) #en Ghz
    max_lo  = models.FloatField(validators=[MinValueValidator (limit_value=8.0), MaxValueValidator(limit_value=110.0)]) #en Ghz

    def __str__(self):
        return self.febe_name
    








class FebeParameters(models.Model):

#    FEBES = [
#        ('febe1', 'Q-XFFTS'),
#        ('febe2', 'W-XFFTS'),
#        ('febe3', 'K-FFTS'),
#        ('febe4', 'CX-FFTS'),
#    ]
    

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    #febe_name = models.CharField(max_length=10, choices= FEBES)
    febe_name = models.ForeignKey(Febes, on_delete=models.CASCADE)
    #febe_string = GenericForeignKey('febe_name', 'febe_name')
    description = models.CharField(max_length=256)
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
    oscillator  = models.FloatField(default = False)

    def __str__(self):
        return self.description
    
    def get_febe_name(self):
        # Accede al objeto Febes relacionado y devuelve su febe_name
        return self.febe_name.febe_name


class Sources(models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=12)
    description = models.CharField(max_length=256)
    offset_eq   = models.BooleanField(default=False)
    offset_hq   = models.BooleanField(default=False)
    reference   = models.FloatField(default = 0.0)

    def __unicode__(self):
        return self.source_name


class Setup (models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    setup_name = models.CharField(max_length=12)
    #aim = models.BooleanField(default=False)
    #cal = models.BooleanField(default=False)
    #foc = models.BooleanField(default=False)
    val_time = models.FloatField(default = 10)
    first_time = models.BooleanField(default=False)

    def __unicode__(self):
        return self.setup_name

class Integrations (models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    integration_name = models.CharField(max_length=12)
    on      = models.BooleanField(default=False)
    onoff   = models.BooleanField(default=False)
    fsw     = models.BooleanField(default=False)
    skydids = models.BooleanField(default=False)
    wobbler = models.BooleanField(default=False)

    def __unicode__(self):
        return self.integration_name
    
class Cal (models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    cal_name = models.CharField(max_length=12)
    calibra = models.BooleanField(default=False)
    cal_time = models.IntegerField(default = 10)
    order = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.cal_name

class Aim (models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    aim_name = models.CharField(max_length=12)
    x_axis = models.FloatField(default = 0)
    y_axis = models.FloatField(default = 0)
    z_axis = models.FloatField(default = 0)
    tilt_x = models.FloatField(default = 0)
    tilt_y = models.FloatField(default = 0)
    single_return = models.BooleanField(default=False)
    samples_number = models.IntegerField(default = 200)
    aim_time = models.FloatField(default = 10)
    order = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.aim_name 

class Foc (models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE)
    foc_name = models.CharField(max_length=12)
    single_return = models.BooleanField(default=False)
    samples_number = models.IntegerField(default = 200)
    foc_time = models.IntegerField(default = 10)
    foc_lenght = models.IntegerField(default = 1)
    order = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.foc_name
