from django.db import models

# Create your models here.

JOB_TYPE = (
  ('Full Time', 'Full Time'),
  ('Part Time', 'Part Time'),

)

class Job(models.Model): # Table
  """
  Represents a job posting in the system.
  Each instance of this model is a separate job listing.
  """
  # Create columns
  title = models.CharField(max_length=100)  # The title of the job posting
  # Location
  job_type = models.CharField(max_length=15, choices=JOB_TYPE)  # Full Time or Part Time
  description = models.TextField(max_length=1000)  # Detailed job description
  published_at = models.DateTimeField(auto_now=True)  # Automatically set when the job is created/updated
  vacancy = models.IntegerField(default=1)  # Number of open positions, default is 1
  salary = models.IntegerField(default=0)  # Annual salary in USD, 0 means 'not specified'
  experience = models.IntegerField(default=1)  # Required years of experience
  category = models.ForeignKey('Category', on_delete=models.CASCADE)


  # Return the column name of the current
  # object (Job object) as a string
  def __str__(self) -> str:
    # return the job title 
    return self.title
  

class Category(models.Model):
  name = models.CharField(max_length=25)

  def __str__(self) -> str:
    # return the Category name
    return self.name


