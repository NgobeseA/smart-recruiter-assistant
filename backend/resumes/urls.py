from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadResumeView.as_view(), name='upload_resume'),
    path('list/', views.ResumeListView.as_view(), name='list_resumes'),
]