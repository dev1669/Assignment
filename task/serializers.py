from rest_framework import serializers
from . models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['contact_person_name','phone_number','address','source','current_stage','last_follow_up_date']

