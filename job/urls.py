from django.urls import path, include
from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'), #return the job with its id

    # API functions methods
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

    # class based views methods
    # path('api/v2/jobs', api.JobListApi.as_view(), name='JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='JobDetail'),
    path('api/v2/jobs', api.JobCreateByApi.as_view(), name='JobCreateByApi'),



]

# experience

