from rest_framework.serializers import ModelSerializer
from .models import Quiz1, Question1


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz1
        fields = ('id', 'name','description','url')


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question1
        fields = "__all__"