from django.db import models

# Create your models here.
class Resume(models.Model):
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.file.name