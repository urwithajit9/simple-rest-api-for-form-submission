from django.contrib import admin
from .models import Chapter, Question, Option

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'description']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'question_type', 'question_text', 'correct_answer']
    list_filter = ['chapter', 'question_type']
