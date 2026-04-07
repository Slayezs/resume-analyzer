from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Resume
from .serializers import ResumeSerializer


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

        serializer = ResumeSerializer(resume)

        return Response(serializer.data, status=201)