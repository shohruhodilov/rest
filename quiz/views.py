from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET','POST'])
def index(request):
    print(request.user)
    print(request.auth)
    print(request.method)
    if request.method=='GET':
        return Response(data={'data':'Hello Django'}, status=status.HTTP_200_OK)
    elif request.method=='POST':
        print(request.data)
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


class Message(APIView):
    def get(self, request):
        return Response(data="class based view to get", status=status.HTTP_200_OK)

    def post(self, request, id):
        print(request.data)
        return Response(data="class based view to post", status=status.HTTP_200_OK)