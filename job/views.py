from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import ApplyForm, JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


def job_list(request):
    job_list = Job.objects.all()  # return all jobs

    # Filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs

    items_per_page = 3  # Change this to your desired number of items per page
    paginator = Paginator(job_list, items_per_page)
    page = request.GET.get('page', 1)

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {'jobs': jobs, 'myfilter':myfilter}  # Template name
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form':form}
    return render(request, 'job/job_detail.html', context)

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form':form})

