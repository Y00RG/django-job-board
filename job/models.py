from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE = (
  ('Full Time', 'Full Time'),
  ('Part Time', 'Part Time'),

)

# Handle uploaded images 
def image_upload(instance, filename):
  image_name, extension = filename.rsplit('.', 1)
  return f'jobs/{instance.id}.{extension}'


class Job(models.Model): # Table
  """
  Represents a job posting in the system.
  Each instance of this model is a separate job listing.
  """
  # Create columns
  owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)  # The title of the job posting
  # Location
  job_type = models.CharField(max_length=15, choices=JOB_TYPE)  # Full Time or Part Time
  description = models.TextField(max_length=1000)  # Detailed job description
  published_at = models.DateTimeField(auto_now=True)  # Automatically set when the job is created/updated
  vacancy = models.IntegerField(default=1)  # Number of open positions, default is 1
  salary = models.IntegerField(default=0)  # Annual salary in USD, 0 means 'not specified'
  experience = models.IntegerField(default=1)  # Required years of experience
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  image = models.ImageField(upload_to=image_upload)
  slug = models.SlugField(blank=True, null=True, unique=True)

  # Override on save() function to modify slug
  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)  # Save the object to get an ID
        # Check if the generated slug already exists
        if Job.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            # Append the object's ID to the slug to make it unique
            self.slug = f'{self.slug}-{self.id}'
            super(Job, self).save(update_fields=['slug'])  # Save again with the updated slug
    else:
        super(Job, self).save(*args, **kwargs)

  # Return the column name of the current
  # object (Job object) as a string
  def __str__(self) -> str:
    # return the job title in admin page
    return self.title
  

class Category(models.Model):
  name = models.CharField(max_length=25)

  def __str__(self) -> str:
    # return the Category name
    return self.name


# Handle apply form
class Apply(models.Model):
  job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  website = models.URLField()
  cv = models.FileField(upload_to='apply/')
  cover_letter = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    # return the Apply name
    return self.name
