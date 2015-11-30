from django.contrib import admin
from school.models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    fields = ['title', 'display_date', 'goal', 'complete', 'time_spent']

admin.site.register(Assignment, AssignmentAdmin)
