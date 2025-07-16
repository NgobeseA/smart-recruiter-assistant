from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import JobPost
from .serializers import JobPostSerializer

# Create your views here.
class CreateJobView(APIView):
    def post(self, request):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def job_detail_view(request):
    jobs = JobPost.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})

def create_job_form_view(request):
    return render(request, 'create_job.html')

def job_list_view(request):
    jobs = JobPost.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})