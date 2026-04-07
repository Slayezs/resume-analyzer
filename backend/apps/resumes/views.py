from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Resume
from .serializers import ResumeSerializer
from .services.parser import extract_text_from_pdf
from .services.extractor import extract_skills

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "No file provided"}, status=400)

        resume = Resume.objects.create(
            user=request.user,
            file=file
        )

        extracted_text = extract_text_from_pdf(resume.file.path)
        resume.extracted_text = extracted_text

        skills = extract_skills(extracted_text)
        resume.extracted_skills = skills

        resume.save()

        return Response({
            "id": resume.id,
            "skills": skills
        }, status=201)