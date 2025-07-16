from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=150, null=True)
    company = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=100, choices=[
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ])
    industry = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(null=True)
    responsibilities = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    bonus_skills = models.TextField(blank=True, null=True)

    required_skills = models.TextField(help_text='Comma-separeted list of required tech skills, e.g. JavaScripts, Python, GitHub', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    Clossing_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} @ {self.company}'