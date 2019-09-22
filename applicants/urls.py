from django.urls import path
from .views import ApplicantsView, NewApplicantForm

urlpatterns = [
    path('', NewApplicantForm.home, name='home'),
    path('api/applicants', ApplicantsView.as_view(), name='applicants'),
    path('api/new_applicant', NewApplicantForm.new_applicant, name='new_applicant')
]
