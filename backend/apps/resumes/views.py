from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Resume
from .serializers import ResumeSerializer
from .services.parser import extract_text_from_pdf

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
        resume.save()

        return Response({
            "id": resume.id,
            "message": "Resume uploaded and parsed successfully"
        }, status=201)