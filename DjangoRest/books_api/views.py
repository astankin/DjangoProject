from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoRest.serializers import BookSerializer
from books_api.models import Book


# Create your views here.
# class ListBookView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response({"books": serializer.data})
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListBookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
