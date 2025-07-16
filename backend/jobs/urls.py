from django.urls import path
from .views import CreateJobView, job_detail_view, create_job_form_view, job_list_view

urlpatterns = [
    path('', job_list_view, name='job_list'),
    path('create/', CreateJobView.as_view(), name='create_job'),
    path('job-details/<int:job_id>/', job_detail_view, name='job_detail'),
    path('form/', create_job_form_view, name='job_form')
]