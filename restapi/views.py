from rest_framework.response import Response
from rest_framework.views import APIView

from restapi.models import users,dataset
from restapi.serializers import UserSerializer,dataSerializer
from rest_framework import status

class UserList(APIView):
    def get(self, request):
        usezx = users.objects.all()
        serializer = UserSerializer(usezx, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DataList(APIView):
    def get(self, request):
        usezx = dataset.objects.all()
        serializer = dataSerializer(usezx, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)