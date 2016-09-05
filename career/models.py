import os
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validation_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extension:
        raise ValidationError(u'Unsupported file extension.')


validation = RegexValidator(regex=r'^0*[1-9][0-9]*(\.[0-9]+)?|0+\.[0-9]*[1-9][0-9]*$', message='Positive Integer only.')
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")

class Profile(models.Model):
    resume = models.FileField(upload_to='resume', validators=[validation_file_extension], verbose_name='Resume')
    name = models.CharField(verbose_name="Name of Candidate", max_length=100, blank=False)
    mobile = models.CharField(verbose_name='Mobile No.', max_length=16, blank=False, validators=[phone_regex])
    email = models.EmailField(unique=True)
    skills = models.CharField(verbose_name='Skills', max_length=200, blank=False)
    work_exp = models.FloatField(verbose_name='Working Experience', validators=[validation])
    analytics_in_exp = models.BooleanField(default=False)
    ctc = models.FloatField(verbose_name='CTC', validators=[validation])
    current_emp = models.CharField(verbose_name='Current Employer', max_length=150, blank=True)
    current_deg = models.CharField(verbose_name='Current Designation', max_length=150, blank=True)
    ug_course = models.CharField(verbose_name='U.G. Course', max_length=30)
    current_location = models.CharField(verbose_name='Current Location', max_length=50, blank=False)
    correct_location = models.CharField(verbose_name='Corrected Location', max_length=50, blank=False)
    near_city = models.CharField(verbose_name='Nearest City', max_length=50, blank=False)
    preferred_location = models.CharField(verbose_name='Preferred Location', max_length=50, blank=False)
    ug_institution = models.CharField(verbose_name='U.G. Institution Name', max_length=150, blank=False)
    trier1 = models.CharField(verbose_name='Trier 1', max_length=2, blank=False)
    ug_year_passing = models.CharField(verbose_name=' U.G. year of passing', max_length=4, blank=False)

    def __str__(self):
        return self.email

    def doc_name(self):
        return self.resume.name.split('/')[-1]  # only the name, not full path



