from django.db import models

class Chapter(models.Model):
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Chapter {self.number}: {self.name}"

class Option(models.Model):
    text = models.CharField(max_length=255)
    # is_correct = models.BooleanField(default=False)  # Mark if this is the correct answer

    def __str__(self):
        return self.text

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]
    
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="questions")
    question_type = models.CharField(max_length=5, choices=QUESTION_TYPE_CHOICES)
    question_text = models.TextField()
    image = models.URLField(max_length=500, null=True, blank=True)
    options = models.ManyToManyField(Option)  # Link to Option model
    correct_answer = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='correct_answers')

    def __str__(self):
        return f"Question {self.id}: {self.question_text}"

    def is_correct(self, answer: Option) -> bool:
        return answer == self.correct_answer
