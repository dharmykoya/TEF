from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Applicant
from .serializers import ApplicantSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
from .forms import ApplicantForm
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q


class ApplicantsView(APIView):
    """
    Provides a get method handler.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'new_applicant.html'

    def get_queryset(self):
        try:
            applicant = Applicant.objects.all()
            return applicant
        except:
            return Response({'message': 'invalid object'})

    def post(self, request,):

        if request.method == "POST":
            # form = ApplicantForm(request.POST)
            data = {key: request.POST[key] for key in request.POST if key !=
                    'csrfmiddlewaretoken'}
        serializer_class = ApplicantSerializer(data=data)
        # serializer_class
        if serializer_class.is_valid():
            serializer_class.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return Response({"message": "something went wrong"})


class NewApplicantForm():

    def new_applicant(request):
        return render(request, 'new_applicant.html')

    def home(request):
        message = ''
        if request.method == 'POST':
            print(121)
            print('post method', request.POST['search'])
            query = request.POST['search']
            applicants = Applicant.objects.filter(
                Q(first_name__contains=query) |
                Q(last_name__contains=query) |
                Q(job_position__contains=query) |
                Q(age__contains=query)
            )
            # applicants = Applicant.objects.all()
            print(333, applicants)
            if not applicants:
                message = 'No results found'
                applicants = Applicant.objects.all()
        else:
            applicants = Applicant.objects.all()
        return render(request, 'index.html', {'applicants': applicants, 'message': message})
    # def home(request):
    #     applicants = Applicant.objects.all()
    #     return render(request, 'index.html', {'applicants': applicants})
