from django.db import models
from django.conf import settings
from account.models import User




class Medication(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    medicine_description = models.CharField(max_length=100, blank=True)
    medicine_type = models.CharField(max_length=15)
    medicine_qty = models.IntegerField(blank=True)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    
    
class Reminder(models.Model):
    date_created = models.DateField(auto_now_add=True)
    medics_id = models.ForeignKey(Medication, on_delete=models.CASCADE)
    medicine_description = models.CharField(max_length=100, blank=True)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    
   

class DocAppointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    doctor_email = models.EmailField(max_length=100, blank=True)
    doctor_phone = models.IntegerField(blank=False)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    
class MedHistory(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='history', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    doctor_name = models.CharField(max_length=100, blank=True)
    desease_name = models.CharField(max_length=100, blank=True)
    
class Frequency(models.Model):
    date_created = models.DateField(auto_now_add=True)
    medics_id = models.ForeignKey(Medication, on_delete=models.CASCADE)
    medicine_desc = models.CharField(max_length=100, blank=True)
    reminder_time = models.TimeField()
    