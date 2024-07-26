from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

# A views but its for the API

#######################################
# function based views methods
# simple - customizable - good in complex work

# function to view all jobs
@api_view(['GET'])
def job_list_api(request):
  all_jobs = Job.objects.all()
  data = JobSerializer(all_jobs, many=True).data

  return Response({'data':data})


# function to view job by its id
@api_view(['GET'])
def job_detail_api(request, id):
  job_detail = Job.objects.get(id=id)
  data = JobSerializer(job_detail).data

  return Response({'data':data})


# Additional methods can be found in the documentation


#######################################
# Class based views methods
# Fast development (less code) - not ideal for complex work

# class method to list all jobs
class JobListApi(generics.ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer


# class method create new jobs through the API
# To use (JobCreateByApi), comment out the (JobListApi) class path in the URLs
class JobCreateByApi(generics.ListCreateAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer


# Class-based view to retrieve, update, and delete a job by its id (3-in-1)
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer
  lookup_field = 'id'

# Additional methods can be found in the documentation

