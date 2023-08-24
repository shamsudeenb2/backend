from .models import Reminder, Medication, MedHistory, DocAppointment, Frequency
from .serializer import ReminderSerializer, MedicSerializer, MedHistorySerializer, DocAptSerializer, FrequencySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
import pytz
newYorkTz = pytz.timezone("Africa/Lagos")


class MedicsView(APIView):
    def get(self, request):
        dateNow = datetime.date(datetime.now())
        timeInNewYork = datetime.now(newYorkTz)
        timeNow = timeInNewYork.strftime("%H:%M:%S")
        all_ilment = Frequency.objects.filter(
            medics_id__patient=self.request.user).filter(
                reminder_time__gt=timeNow
            )[:5]
        serializer = FrequencySerializer(all_ilment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        patient = self.request.user.id
        request.data['patient'] = patient
        
        serializerM = MedicSerializer(data=request.data)
        if serializerM.is_valid():
            medic_instance = serializerM.save()

            frequency_data_list = request.data.get('frequency', [])  # Use get() with a default value of []

            saved_reminders = []
            
            for frequency_data in frequency_data_list:
                frequency_data['medics_id'] = medic_instance.id
                print(frequency_data)
                serializer = FrequencySerializer(data=frequency_data)
                
                if serializer.is_valid():
                    serializer.save()
                    saved_reminders.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(saved_reminders, status=status.HTTP_201_CREATED)
        else:
            return Response(serializerM.errors, status=status.HTTP_400_BAD_REQUEST)

        
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None,format=None):
        data = request.data
        # qs = Medication.objects.filter(pk=pk).update(medicine_qty=request.data.get('medicine_qty'))
        qs = Medication.objects.get(pk=pk)
        serializer = MedicSerializer(qs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
       
    def delete(self, request, pk=None):
        med = Frequency.objects.filter(pk=pk)
        med.delete()
        return Response('Delete Successfully', status=status.HTTP_200_OK)



class MedHistoryView(APIView):
    
    def get(self, request):
        history = MedHistory.objects.filter(patient=self.request.user)[:5]
        serializer = MedHistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        patient = self.request.user.id
        request.data['patient'] = patient
        serializer = MedHistorySerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk=None,format=None):
        data = request.data
        # qs = MedHistory.objects.filter(pk=pk).update(request.data)
        qs=MedHistory.objects.get(pk=pk)
        serializer = MedHistorySerializer(qs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error)
        
    
    def delete(self, request, pk=None):
        drinks = MedHistory.objects.filter(pk=pk)
        drinks.delete()
        return Response('Delete Successfully', status=status.HTTP_200_OK)


class AppointmentView(APIView):
    def get(self, request):
        dateNow = datetime.date(datetime.now())
        timeInNewYork = datetime.now(newYorkTz)
        timeNow = timeInNewYork.strftime("%H:%M:%S")
        history = DocAppointment.objects.filter(patient=self.request.user).filter(
                reminder_time__gt=timeNow
                ).filter(
                reminder_date=dateNow
            )[:5]
        serializer = DocAptSerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        patient = self.request.user.id
        request.data['patient'] = patient
        serializer = DocAptSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk=None,format=None):
        data = request.data
        qs = DocAppointment.objects.get(pk=pk)
        serializer = DocAptSerializer(qs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error)
        
    def delete(self, request, pk=None):
        drinks = DocAppointment.objects.filter(pk=pk)
        drinks.delete()
        return Response('Delete Successfully', status=status.HTTP_200_OK)
    
    
class HomeView(APIView):
    
    def get(self, request):
        dateNow=datetime.now().strftime ("%Y-%m-%d")
        timeInNewYork = datetime.now(newYorkTz)
        timeNow = timeInNewYork.strftime("%H:%M:%S")
        med = Reminder.objects.filter(
            medics_id__patient=self.request.user).filter(
                reminder_time__gt=timeNow
            )[:1]
        remi_serializer = ReminderSerializer(med, many=True)
    
        appt = DocAppointment.objects.filter(
              patient=self.request.user).filter(
                reminder_time__gte=timeNow, reminder_date__gte=dateNow
            )[:1]
        appt_serializer = DocAptSerializer(appt, many=True)
        
        medics = Medication.objects.filter(
            patient=self.request.user).filter(
                reminder_time__gt=timeNow
            )[:1]
        med_serializer = MedicSerializer(medics, many=True)
        
        data = med_serializer.data + appt_serializer.data + remi_serializer.data
        
        return Response(data, status=status.HTTP_200_OK)



class ReminderView(APIView):
       
    def get(self, request):
        dateNow = datetime.date(datetime.now())
        timeInNewYork = datetime.now(newYorkTz)
        timeNow = timeInNewYork.strftime("%H:%M:%S")
        all_ilment = Reminder.objects.filter(
            medics_id__patient=self.request.user).filter(
                reminder_time__gt=timeNow
            )[:5]
        serializer = ReminderSerializer(all_ilment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ReminderSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def put(self, request, pk=None,format=None):
        # qs = Medication.objects.filter(pk=pk).update(medicine_qty=request.data.get('medicine_qty'))
        data = request.data
        qs = Medication.objects.get(pk=pk)
        serializer = MedicSerializer(qs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error)
       
       
        
    def delete(self, request, pk=None):
        rem = Reminder.objects.filter(pk=pk)
        rem.delete()
        return Response('Delete Successfully', status=status.HTTP_200_OK)
    

class GetAllMedics(APIView):
    def get(self, request):
        all_ilment = Medication.objects.filter(patient=self.request.user)
        serializer = MedicSerializer(all_ilment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
