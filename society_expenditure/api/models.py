import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Exp(AbstractUser):
    user_name = models.CharField(max_length = 100, default='NULL')
    securityquestion = models.CharField(max_length = 100, default = '')
    securityanswer = models.CharField(max_length = 100, default = '')
    password = models.CharField(max_length = 100 , default='')

    def set_password(self, raw_password):
        # Hash the password using make_password before saving it
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Check if the provided raw password matches the stored hashed password
        return check_password(raw_password, self.password)
class Content(models.Model):
    user = models.ForeignKey(Exp, on_delete=models.CASCADE)
    name =  models.CharField(max_length = 100, default='NULL')
    event = models.CharField(max_length = 100, default='NULL')
    Date = models.DateField(default=datetime.date(2023, 12, 24))
    Current_Balance = models.DecimalField(max_digits = 20 , decimal_places = 2 , default = 0.00)
    Total_Amount = models.DecimalField(max_digits = 20 , decimal_places = 2 , default = 0.00)
    Total_Spent = models.DecimalField(max_digits = 20 , decimal_places = 2 , default = 0.00)

class UserProfile(models.Model):
    user = models.OneToOneField(Exp, on_delete=models.CASCADE)
    fats = models.BooleanField(default=False)
    cult = models.BooleanField(default=False)
    paracosm = models.BooleanField(default=False)
    photogeeks = models.BooleanField(default=False)
    tech = models.BooleanField(default=False)
    vedant = models.BooleanField(default=False)
    megaheartz = models.BooleanField(default=False)
    tars = models.BooleanField(default=False)
    ecell = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
    

