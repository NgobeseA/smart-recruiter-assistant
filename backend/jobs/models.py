from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ])
    industry = models.CharField(max_length=100, blank=True)

    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    bonus_skills = models.TextField(blank=True)

    required_skills = models.TextField(help_text='Comma-separeted list of required tech skills, e.g. JavaScripts, Python, GitHub')
    created_at = models.DateTimeField(auto_now_add=True)
    Clossing_date = models.DateField()

    def __str__(self):
        return f'{self.title} @ {self.company}'