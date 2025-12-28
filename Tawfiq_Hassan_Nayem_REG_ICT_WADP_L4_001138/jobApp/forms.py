from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, RecruiterProfile, JobSeekerProfile, Job



class UserRegistrationForm(UserCreationForm):
    display_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = (
            'username',
            'display_name',
            'email',
            'password1',
            'password2',
            'user_type',
        )



class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = (
            'company_name',
            'email',
            'phone',
            'company_website',
        )


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = (
            'skills',
            'resume',
        )


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            'title',
            'number_of_openings',
            'category',
            'job_description',
            'skills_required',
            'location',
            'salary',
        )
