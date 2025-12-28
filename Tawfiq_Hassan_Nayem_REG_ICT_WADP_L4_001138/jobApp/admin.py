from django.contrib import admin
from .models import User, RecruiterProfile, JobSeekerProfile, Job, JobApplication

admin.site.register(User)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)
admin.site.register(Job)
admin.site.register(JobApplication)

