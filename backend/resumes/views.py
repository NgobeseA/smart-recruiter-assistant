from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pdfplumber

from .models import Resume
from .serializers import ResumeSerializer

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

class ResumeListView(APIView):
    pass