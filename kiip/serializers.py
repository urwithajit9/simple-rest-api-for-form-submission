from rest_framework import serializers
from .models import Question, Option, Chapter

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [ 'text']  # You can add other fields as needed

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    correct_answer = OptionSerializer()

    class Meta:
        model = Question
        fields = ['id', 'question_type', 'question_text', 'image', 'options', 'correct_answer']

class ChapterQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ['number', 'name', 'description', 'questions']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'number', 'name', 'description']        
