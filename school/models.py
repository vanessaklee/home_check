from django.db import models
import datetime

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    goal = models.CharField(max_length=255)
    display_date = models.DateField(default=datetime.date.today)
    complete = models.BooleanField(default=False, verbose_name=b'Are you finished with this assignment?')
    time_spent = models.TimeField()


