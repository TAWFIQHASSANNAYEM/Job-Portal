from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import User, RecruiterProfile, JobSeekerProfile, Job, JobApplication
from .forms import JobForm, RecruiterProfileForm, JobSeekerProfileForm, UserRegistrationForm

def home(request):
    jobs = Job.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'jobs': jobs})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def create_profile(request):
    if request.user.user_type == 'recruiter':
        if request.method == 'POST':
            form = RecruiterProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('dashboard')
        else:
            form = RecruiterProfileForm()
        return render(request, 'create_recruiter_profile.html', {'form': form})
    else:
        if request.method == 'POST':
            form = JobSeekerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('dashboard')
        else:
            form = JobSeekerProfileForm()
        return render(request, 'create_jobseeker_profile.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.user_type == 'recruiter':
        profile = RecruiterProfile.objects.get(user=request.user)
        jobs = Job.objects.filter(recruiter=request.user)
        total_jobs = jobs.count()
        total_applications = JobApplication.objects.filter(job__recruiter=request.user).count()
        pending_applications = JobApplication.objects.filter(job__recruiter=request.user, status='pending').count()
        accepted_applications = JobApplication.objects.filter(job__recruiter=request.user, status='accepted').count()
        return render(request, 'recruiter_dashboard.html', {
            'profile': profile,
            'jobs': jobs,
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'accepted_applications': accepted_applications
        })
    else:
        profile = JobSeekerProfile.objects.get(user=request.user)
        applied_applications = JobApplication.objects.filter(jobseeker=request.user).select_related('job')
        applied_job_ids = applied_applications.values_list('job_id', flat=True)
        matched_jobs = Job.objects.filter(
            Q(skills_required__icontains=profile.skills) |
            Q(title__icontains=profile.skills)
        ).exclude(id__in=applied_job_ids)
        total_applications = applied_applications.count()
        pending_applications = applied_applications.filter(status='pending').count()
        accepted_applications = applied_applications.filter(status='accepted').count()
        return render(request, 'jobseeker_dashboard.html', {
            'profile': profile,
            'matched_jobs': matched_jobs,
            'applied_applications': applied_applications,
            'applied_job_ids': applied_job_ids,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'accepted_applications': accepted_applications
        })

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})

def all_jobs(request):
    from django.core.paginator import Paginator
    jobs = Job.objects.all().order_by('-created_at')
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_jobs.html', {'page_obj': page_obj})

@login_required
def search_jobs(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(job_description__icontains=query) | Q(skills_required__icontains=query))
    if category:
        jobs = jobs.filter(category=category)
    if location:
        jobs = jobs.filter(location__icontains=location)
    return render(request, 'search_jobs.html', {'jobs': jobs, 'query': query, 'category': category, 'location': location})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if JobApplication.objects.filter(job=job, jobseeker=request.user).exists():
        messages.info(request, 'You have already applied for this job.')
    else:
        JobApplication.objects.create(job=job, jobseeker=request.user)
        messages.success(request, 'Application submitted successfully.')
    return redirect('dashboard')

@login_required
def edit_recruiter_profile(request):
    profile = get_object_or_404(RecruiterProfile, user=request.user)
    if request.method == 'POST':
        form = RecruiterProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RecruiterProfileForm(instance=profile)
    return render(request, 'edit_recruiter_profile.html', {'form': form})

@login_required
def edit_jobseeker_profile(request):
    profile = get_object_or_404(JobSeekerProfile, user=request.user)
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobSeekerProfileForm(instance=profile)
    return render(request, 'edit_jobseeker_profile.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard')
    return render(request, 'delete_job.html', {'job': job})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def view_applicants(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)
    applications = JobApplication.objects.filter(job=job).select_related('jobseeker__jobseekerprofile')
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        status = request.POST.get('status')
        application = get_object_or_404(JobApplication, id=application_id, job=job)
        application.status = status
        application.save()
        return redirect('view_applicants', job_id=job_id)
    return render(request, 'view_applicants.html', {'job': job, 'applications': applications})
