from .models import Medication, Reminder, DocAppointment, MedHistory, Frequency
from rest_framework import serializers
from datetime import datetime
import pytz
newYorkTz = pytz.timezone("Africa/Lagos") 
        




class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
        
    def perform_create(self, serializer):
        patient = self.request.user.id
        serializer.validated_data['patient'] = patient
        serializer.save()

class ReminderSerializer(serializers.ModelSerializer):
    medics_id = serializers.PrimaryKeyRelatedField(queryset=Medication.objects.all())
    class Meta:
        model = Reminder
        fields = '__all__'
    
    def create(self, validated_data):
        medication_id = validated_data.pop('medics_id')
        reminder = Reminder.objects.create(medics_id=medication_id, **validated_data)
        return reminder


class DocAptSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAppointment
        fields = '__all__'
       


class MedHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedHistory
        fields = '__all__'
        
        
class FrequencySerializer(serializers.ModelSerializer):
    medics_id = serializers.PrimaryKeyRelatedField(queryset=Medication.objects.all())
    class Meta:
        model = Frequency
        fields = '__all__'
    
    def create(self, validated_data):
        medication_id = validated_data.pop('medics_id')
        reminder = Frequency.objects.create(medics_id=medication_id, **validated_data)
        return reminder