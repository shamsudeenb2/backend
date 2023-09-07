from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import Med, Apointment, RefilReminder

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(RefilReminder, 'interval', seconds=1800)
    scheduler.add_job(Apointment, 'interval', seconds=1800)
    scheduler.add_job(Med, 'interval', seconds=1800)
    scheduler.start() 