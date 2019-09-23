from django import forms
from .models import Applicant

class ApplicantForm(forms.Form):
    model = Applicant

    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    age = forms.IntegerField()
    job_position = forms.CharField(max_length= 100)


