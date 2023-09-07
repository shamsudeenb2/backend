from django.urls import path
from . import views


urlpatterns = [
    # path("home/", views.HomeView.as_view(), name="home"),
    
    path("medics/", views.MedicsView.as_view(), name="medics"),
    path("all/", views.GetAllMedics.as_view(), name="medics_all"),
    
    path("medics/<int:pk>/", views.MedicsView.as_view(), name="medics_update"),
    
    path("records/", views.MedHistoryView.as_view(), name="Record"),
    
    path("records/<int:pk>/", views.MedHistoryView.as_view(), name="record_update"),
    
    path("appoint/", views.AppointmentView.as_view(), name="appointment"),
    path("appoint/<int:pk>/", views.AppointmentView.as_view(), name="appoint_update"),
    
    path("reminder/", views.ReminderView.as_view(), name="reminder"),
    path("reminder/<int:pk>/", views.ReminderView.as_view(), name="reminder")
]