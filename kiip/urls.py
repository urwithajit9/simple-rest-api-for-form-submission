from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChapterQuestionsViewSet, ChapterViewSet

router = DefaultRouter()
router.register(r'chapterwisedquestions', ChapterQuestionsViewSet, basename='chapter-questions')
router.register(r'chapter', ChapterViewSet, basename='chapter')

urlpatterns = [
    path('kiip/', include(router.urls)),
]
