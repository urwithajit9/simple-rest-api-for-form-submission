from rest_framework import viewsets
from rest_framework.response import Response
from .models import Chapter
from .serializers import ChapterQuestionsSerializer, ChapterSerializer

class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()  # Fetch all chapters
    serializer_class = ChapterSerializer

    def list(self, request, *args, **kwargs):
        # Return all chapters as a list
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ChapterQuestionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()  # Assuming you have a Chapter model with related questions
    serializer_class = ChapterQuestionsSerializer

    def retrieve(self, request, *args, **kwargs):
        chapter = self.get_object()  # Get the specific chapter object
        serializer = self.get_serializer(chapter)
        return Response(serializer.data)
