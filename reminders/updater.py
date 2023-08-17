from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import Med

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(Med, 'interval', seconds=5)
	scheduler.start() 