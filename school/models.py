from django.db import models
import datetime

class Resource(models.Model):
    title = models.CharField(max_length=255, verbose_name=b'Name of the resource?')
    cover = models.ImageField(upload_to=None, max_length=100, blank=True, null=True)

    def __str__(self):
      return self.title

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField(max_length=1000, blank=True)
    resource = models.ForeignKey(Resource, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    goal = models.TextField(max_length=1000, blank=True, null=True)
    display_date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    complete = models.BooleanField(default=False, verbose_name=b'Are you finished with this assignment?')
    time_spent = models.TimeField(blank=True, null=True)

    def __str__(self):
      return self.title

    def is_due_today(self):
      return self.due_date == datetime.date.today()


