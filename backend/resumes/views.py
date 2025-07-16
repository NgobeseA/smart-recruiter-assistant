from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pdfplumber

from .models import Resume
from .serializers import ResumeSerializer
from jobs.models import JobPost
from scoring.scoring_engine import semantic_score, evaluate_resume

# Create your views here.
class UploadResumeView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            print('The form is valid')
            resume = serializer.save()
            print(resume)

            cv = resume.file.path
            with pdfplumber.open(cv) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                resume.parsed_text = text
                print(text)
                resume.save()

            return Response(ResumeSerializer(resume).data, status=status.HTTP_201_CREATED)
        return Response({
            'error': 'Invalid data',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ResumeListWithScoreView(APIView):
    def get(self, request, job_id):
        try:
            job = JobPost.objects.get(id=job_id)
        except JobPost.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
        
        resumes = Resume.object.filter(job=job)
        results = []

        required_skills = job.required_skills.split(',') if job.required_skills else []

        for resume in resumes:
            feedback = evaluate_resume(resume.parsed_text, job.description,required_skills)
            data = ResumeSerializer(resume).data
            data["semantic_score"] = feedback["semantic_score"]
            data["matched_skills"] = feedback["matched_skills"]
            data["missing_skills"] = feedback["missing_skills"]
            results.append(data)
            
        return Response(results, status=status.HTTP_200_OK)
