from rest_framework import serializers
from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant

        fields = ("first_name", "last_name", "age", "job_position")
        # first_name = serializers.CharField(
        #     max_length=100,
        #     style={'placeholder': 'First Name', 'autofocus': True}
        # )

        # last_name = serializers.CharField(
        #     max_length=100,
        #     style={'placeholder': 'Last Name', 'autofocus': True}
        # )

        # age = serializers.IntegerField(
        #     style={'placeholder': 'Age', 'autofocus': True}
        # )

        # job_position = serializers.CharField(
        #     max_length=100,
        #     style={'placeholder': 'Job', 'autofocus': True}
        # )
