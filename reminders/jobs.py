from django_apscheduler.jobstores import DjangoJobStore, register_events
from medication.models import Medication, Reminder,DocAppointment
# from account.models import User
from datetime import datetime, timedelta
import pytz
newYorkTz = pytz.timezone("Africa/Lagos")


def Med():
    dateNow = datetime.date(datetime.now())
    timeInNewYork = datetime.now(newYorkTz)
    timeNow = timeInNewYork.strftime("%H:%M:%S")
    result_1 = timeNow 
    
    meds = Medication.objects.all().filter(
        reminder_time__gt=result_1
    )
    
    for data in meds:
        # user=User.objects.filter(email=data.patient)
        print(data)







# Register the Django job store and scheduler events
# scheduler.add_jobstore(DjangoJobStore(), 'default')
# register_events(scheduler)