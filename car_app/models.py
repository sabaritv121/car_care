from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    emp_id = models.CharField(max_length=10)



class AppointmentSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()  
    is_active = models.BooleanField(default=True)  



class Appointment(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)    