from django_apscheduler.jobstores import DjangoJobStore, register_events
from medication.models import Medication, Reminder, DocAppointment, Frequency
from medication.serializer import ReminderSerializer, MedicSerializer, MedHistorySerializer, DocAptSerializer, FrequencySerializer
from account.models import User
from datetime import datetime, timedelta
import pytz
import os
newYorkTz = pytz.timezone("Africa/Lagos")
from django.conf import settings
from twilio.rest import Client 

twilio_account_sid = settings.TWILIO_ACCOUNT_SID
twilio_auth_token = settings.TWILIO_AUTH_TOKEN
twilio_phone_number = settings.TWILIO_NUMBER
client = Client(twilio_account_sid, twilio_auth_token)

def send_sms(phone_number, msg):
      
    message = client.messages.create(
        body= msg ,
        from_=twilio_phone_number,
        to=phone_number
    )
    
    print("SMS sent for reminder")
    

def Med():
    # dateNow = datetime.date(datetime.now(newYorkTz))
    timeInNewYork = datetime.now(newYorkTz)
    result1= timeInNewYork + timedelta(hours=1)
    timeNow = timeInNewYork.strftime("%H:%M:%S")
    timeNow1 = result1.strftime("%H:%M:%S")
    print('Med Reminder')
    meds = Frequency.objects.all().filter(
        reminder_time__gte=timeNow,
        reminder_time__lte=timeNow1
    )
    # t1 = datetime.strptime(timeNow, "%H:%M:%S")
    # t1 = datetime.utcnow().replace(tzinfo=pytz.timezone("Africa/Lagos"))
    
    if meds:
        for data in meds:
            user=User.objects.all().values_list('phone_number').get(email=data.medics_id.patient)
            medname = Medication.objects.all().values_list('name').get(id=data.medics_id.id)
            # send_sms(user[0],)
            # data.medics_id.patient,data.reminder_time,
            # t2 = data.reminder_time.strptime("%H:%M:%S")
            # delta = data.reminder_time - t1.time()
            msg = f'Reminder for taking {medname[0]} at {data.reminder_time}'
            
            print(user[0], data.medics_id.patient, msg)
            send_sms(user[0], msg)

def RefilReminder():
    dateNow = datetime.date(datetime.now(newYorkTz))
    timeInNewYork = datetime.now(newYorkTz)
    result1= timeInNewYork + timedelta(hours=1)
    timeNow = timeInNewYork.strftime("%H:%M:%S")
    timeNow1 = result1.strftime("%H:%M:%S")
    result_1 = timeNow 
    print('RefilReminder')
    refil=Reminder.objects.all().filter(
                reminder_time__gte=result_1,
                reminder_time__lte=timeNow1
            ).filter(reminder_date=dateNow)
    
    if refil:
        for data in refil:
            user=User.objects.all().values_list('phone_number').get(email=data.medics_id.patient)
            medname = Medication.objects.all().values_list('name').get(id=data.medics_id.id)
            msg = f'Reminder to refill {medname[0]} on {data.reminder_date} at {data.reminder_time}'
            
            print(data.medics_id.patient,data.reminder_time, user[0])
            send_sms(user[0], msg)


def Apointment():
    dateNow = datetime.date(datetime.now(newYorkTz))
    timeInNewYork = datetime.now(newYorkTz)
    result1= timeInNewYork + timedelta(hours=1)
    timeNow = timeInNewYork.strftime("%H:%M:%S")
    timeNow1 = result1.strftime("%H:%M:%S")
    result_1 = timeNow 
    print('Apointment')
    appoint=DocAppointment.objects.all().filter(
                reminder_time__gte=result_1,
                reminder_time__lte=timeNow1
                ).filter(
                reminder_date=dateNow
                )
    
    
    if appoint:
        for data in appoint:
            user=User.objects.all().values_list('phone_number').get(email=data.patient)
            medname = Medication.objects.all().values_list('name').get(id=data.medics_id.id)
            msg = f'Your Appointment with {data.name} is on {data.reminder_date} at {data.reminder_time}'
            print(data.patient,data.reminder_time, user[0])
            send_sms(user[0], msg)



# Register the Django job store and scheduler events
# scheduler.add_jobstore(DjangoJobStore(), 'default')
# register_events(scheduler)