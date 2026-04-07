from django.db import models
from apps.resumes.models import Resume

class AnalysisResult(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description = models.TextField()

    match_score = models.FloatField()
    ats_score = models.FloatField()

    matched_skills = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)