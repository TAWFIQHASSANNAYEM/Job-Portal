from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'Job Seeker'),
    )

    display_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(Group, related_name='jobapp_user', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='jobapp_user_permission', blank=True)

    def __str__(self):
        return self.username


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_description = models.TextField()
    company_website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.company_name


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username


class Job(models.Model):
    CATEGORY_CHOICES = (
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
        ('manager', 'Manager'),
        ('other', 'Other'),
    )
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    number_of_openings = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='junior')
    job_description = models.TextField()
    skills_required = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.jobseeker.username} - {self.job.title}"
