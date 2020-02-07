from django.shortcuts import render
from rest_framework.decorators import api_view
from own.models import Question1, Quiz1
from own.serializers import QuizSerializer, QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET','POST'])
def hello(request):
    print(request.method)
    if request.method=='GET':
        return Response('{salom: Salom Dunyo}')
    elif request.method=='POST':
        return Response(data=request.data, status=status.HTTP_201_CREATED)
    else:
        return Response('Not Found')


class Mana(APIView):
    def get_obj(self, pk):
        try:
            queryset = Quiz1.objects.get(pk=pk)
            return queryset
        except ModuleNotFoundError:
            return Response('Module topilmadi')
    def get(self, request, pk):
        queryset = self.get_obj(pk)
        serializer = QuizSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, pk):
        print(request.data)
        serializer = QuizSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            print(serializer)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request,pk, format=None):
        queryset = self.get_obj(pk)
        queryset.delete()
        # print(queryset)
        # print(request.data)
        # print(id)
        # queryset.delete()
        return Response(data='Deleted',status=status.HTTP_410_GONE)



class Man(APIView):
    def get_obj(self):
        try:
            queryset = Quiz1.objects.all()
            return queryset
        except ModuleNotFoundError:
            return Response('Module topilmadi')
    def get(self, request):
        queryset = self.get_obj()
        serializer = QuizSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        print(request.data)
        serializer = QuizSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            print(serializer)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
