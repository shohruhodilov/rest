from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question, Quiz
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework.response import Response
from rest_framework import status

class QuizView(APIView):
    def get_object(self):
        try:
            return Quiz.objects.all()
        except Quiz.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request):
        queryset = self.get_object()
        serializer = QuizSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        queryset = Quiz.objects.get(id=2)
        queryset.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)
