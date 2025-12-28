from django.urls import path
from .views import home, register, user_login, create_profile, dashboard, post_job, all_jobs, search_jobs, apply_job, edit_recruiter_profile, edit_jobseeker_profile, edit_job, delete_job, view_applicants, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('create_profile/', create_profile, name='create_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('post_job/', post_job, name='post_job'),
    path('all_jobs/', all_jobs, name='all_jobs'),
    path('search_jobs/', search_jobs, name='search_jobs'),
    path('apply_job/<int:job_id>/', apply_job, name='apply_job'),
    path('edit_recruiter_profile/', edit_recruiter_profile, name='edit_recruiter_profile'),
    path('edit_jobseeker_profile/', edit_jobseeker_profile, name='edit_jobseeker_profile'),
    path('edit_job/<int:job_id>/', edit_job, name='edit_job'),
    path('delete_job/<int:job_id>/', delete_job, name='delete_job'),
    path('view_applicants/<int:job_id>/', view_applicants, name='view_applicants'),
    path('logout/', user_logout, name='logout'),
]
