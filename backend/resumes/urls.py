from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('upload/', views.UploadResumeView.as_view(), name='upload_resume'),
    path('list/', views.ResumeListView.as_view(), name='list_resumes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)