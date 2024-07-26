from rest_framework import serializers
from .models import Job

# serializers get data from model and return it as json data
# to be able to link your app to another framework or a mobile app


class JobSerializer(serializers.ModelSerializer):
  class Meta:
    model = Job
    fields = '__all__'
