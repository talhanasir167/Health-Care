from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class PatientInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address=models.CharField(max_length=40)
    gender=models.CharField( max_length=50,default='Male',choices=(('Female','Female'),('Male','Male'),('Other','Other')))
    age=models.CharField(default=18, max_length=20)
    status=models.CharField(max_length=20,default='Single',choices=(('Single','Single'),('Married','Married')))
    profile_pic=models.ImageField(blank=True,null=True)

