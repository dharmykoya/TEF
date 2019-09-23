from rest_framework import serializers
from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant

        fields = ("first_name", "last_name", "age", "job_position")
       
