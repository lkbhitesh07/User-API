from django.db.models.query import QuerySet
from django.http.response import Http404
from .serializers import UserSerializer, RestrictedUserSerializer
from .models import CustomUser
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import CustomPageNumberPagination


# Create your views here.
class UserAPIView(APIView):
    # queryset = CustomUser.objects.all()
    # serializer_class = UserSerializer
    # pagination_class = CustomPageNumberPagination



    serializer_class = UserSerializer

    def get(self, request, format=None):
        data = CustomUser.objects.all()
        page = self.request.GET.get('page', 1)
        limit = self.request.GET.get('limit', 5)
        name = self.request.GET.get('name')
        sort = self.request.GET.get('sort')

        if name:
            data = data.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if sort == 'age':
            data = data.order_by('age')
        elif(sort == '-age'):
            data = data.order_by('-age')

        if page:
            page = int(page)
        
        if limit:
            limit = int(limit)

        start = (page-1) * limit
        end = page * limit

        serializer = self.serializer_class(data[start:end], many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleUserAPIView(APIView):
    serializer_class = RestrictedUserSerializer

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)

# This methods helps in creating multiple users at once.

class MultipleUserAPIView(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):
        length_data = len(request.data)
        for ele in range(length_data):
            serializer = self.serializer_class(data=request.data[ele])
            if serializer.is_valid():
                serializer.save()
                serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_201_CREATED)



