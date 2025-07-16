from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import JobPost
from .serializers import JobPostSerializer

# Create your views here.
class CreateJobView(APIView):
    def post(self, request):
        data = request.data
        print(f"Data from the API: {data}")
        serializer = JobPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def job_detail_view(request, job_id):
    print(f'Job Id: {job_id}')
    job = JobPost.objects.filter(pk=job_id).first()
    return render(request, 'job_detail.html', {'job': job})

def create_job_form_view(request):
    return render(request, 'create_job.html')

def job_list_view(request):
    jobs = JobPost.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})