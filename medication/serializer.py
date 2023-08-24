from .models import Medication, Reminder, DocAppointment, MedHistory, Frequency
from rest_framework import serializers
from datetime import datetime
import pytz
newYorkTz = pytz.timezone("Africa/Lagos") 
        


class MedicSerializer(serializers.ModelSerializer):
    # medics_id = FrequencySerializer(many=True, read_only=True)
    class Meta:
        model = Medication
        fields = '__all__'
        # ['patient', 'name', 'medicine_type', 'medicine_qty', 'reminder_date', 'reminder_time', 'medics_id']
        
    def perform_create(self, serializer):
        patient = self.request.user.id
        serializer.validated_data['patient'] = patient
        serializer.save()

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
    
    def create(self, validated_data):
        medication_id = validated_data.pop('medics_id')
        reminder = Reminder.objects.create(medics_id=medication_id, **validated_data)
        return reminder
    
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        
        medic = instance.medics_id
        custom_medic_representation = {
            'id': medic.id,
            'name': medic.name,
            'medicine_qty': medic.medicine_qty,
            'reminder_date': medic.reminder_date,
            'reminder_time': medic.reminder_time,
            'medicine_type': medic.medicine_type,
            'medicine_description': medic.medicine_description,
            'date_created': medic.date_created,
            # Add more fields as needed
        }

        representation['medics'] = custom_medic_representation

        return representation

class DocAptSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocAppointment
        fields = '__all__'
       


class MedHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedHistory
        fields = '__all__'
        
class FrequencySerializer(serializers.ModelSerializer):
    # medics_id = serializers.PrimaryKeyRelatedField(queryset=Medication.objects.all())
    # medics_id = MedicSerializer()
    # medics_id = serializers.IntegerField()
    class Meta:
        model = Frequency
        fields = '__all__'
        
    
    def create(self, validated_data):
        medication_id = validated_data.pop('medics_id')
        reminder = Frequency.objects.create(medics_id=medication_id, **validated_data)
        return reminder
    
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        
        medic = instance.medics_id
        custom_medic_representation = {
            'id': medic.id,
            'name': medic.name,
            'medicine_qty': medic.medicine_qty,
            'reminder_date': medic.reminder_date,
            'reminder_time': medic.reminder_time,
            'medicine_type': medic.medicine_type,
            'medicine_description': medic.medicine_description,
            'date_created': medic.date_created,
            # Add more fields as needed
        }

        representation['medics'] = custom_medic_representation

        return representation
    #     data["medics_id"]=MedicSerializer(instance.medics_id).data