from django.db import models

# Create your models here.
from django.db import models
class Agency(models.Model):
    name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=100,null=True)
    id_number = models.CharField(max_length=20,null=True)
    def _str_(self):
        return str(self.name)
    
class Register(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    def _str_(self):
        return str(self.username)
      


# Create your models here.

    
class Agent_Register(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    
    def _str_(self):
        return self.username
    from django.utils import timezone
    from django.core import validators



class bookdetails(models.Model):
    #time_field = models.TimeField(validators=[validators.TimeValidator()])
    date1 = models.DateField()
    date2 = models.DateField()
    pickup = models.TimeField()
    fro =models.CharField(max_length=100,null=True)
    
    to =models.CharField(max_length=100,null=True)
    available = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.date1} {self.date2} {self.pickup}  {self.fro} {self.to} ({'Available' if self.available else 'Booked'}) "
        
class Vehicle(models.Model):
    name=models.CharField(max_length=255,null=True)
    number=models.IntegerField()
    driver=models.CharField(max_length=255,null=True)
    type=models.CharField(max_length=255)
    fare=models.IntegerField()
    seats=models.IntegerField()
    image=models.ImageField(upload_to='images/',null=True)
    #def _str_(self):
        #return str(self.name)
    available = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.name} {self.number} {self.driver}  {self.type} {self.fare} ({'Available' if self.available else 'Booked'}) "
    

