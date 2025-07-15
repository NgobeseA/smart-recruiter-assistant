from django.db import models
from jobs.models import JobPost

# Create your models here.
class Resume(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.file.name