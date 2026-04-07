from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.resumes.models import Resume
from .models import AnalysisResult
from .services.matcher import match_resume_with_job
from .services.ats_score import calculate_ats_score


class AnalyzeResumeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        resume_id = request.data.get("resume_id")
        job_description = request.data.get("job_description")

        resume = Resume.objects.get(id=resume_id)

        # Matching
        result = match_resume_with_job(
            resume.extracted_skills,
            job_description
        )

        # ATS Score
        ats_score = calculate_ats_score(
            result["match_score"],
            resume.extracted_skills
        )

        # Save result
        analysis = AnalysisResult.objects.create(
            resume=resume,
            job_description=job_description,
            match_score=result["match_score"],
            ats_score=ats_score,
            matched_skills=result["matched_skills"],
            missing_skills=result["missing_skills"]
        )

        return Response({
            "match_score": analysis.match_score,
            "ats_score": analysis.ats_score,
            "matched_skills": analysis.matched_skills,
            "missing_skills": analysis.missing_skills
        })