from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.schemas import AutoSchema



# Create your views here.
class BookView(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(
        operation_id='Get_Books',
        operation_description='Get all the book list from the database.',
        )
    def get(self,request):
        queryset= Books.objects.all()
        serializer=BookSerializer(queryset,many=True)
        return Response(serializer.data)
    
class BookPostView(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(
        request_body=BookSerializer,
        # query_serializer=BookSerializer,
        responses={
            '201': 'Book Posted',
            '400': "Bad Request"
        },
        security=[],
        operation_id='POST_Book',
        operation_description='Insert book into database',
        )
    def post(self,request,format=None):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

class BookDetail(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
        
    
    def get_post(self,pk):
        try:
            return Books.objects.get(isbn=pk)
        except:
            return nothing
            pass
    @swagger_auto_schema(
        operation_id='Get_Books_By_Isdn',
        operation_description='Get books by ISBN number. [id is ISBN]',
        )
    def get(self,request,pk):
            try:
                book= self.get_post(pk)
                serializer=BookSerializer(book)
                return Response(serializer.data)
            except:
                data={}
                data['message']='ISBN does not match any book.'
                return Response(data)

    @swagger_auto_schema(
        request_body=BookSerializer,
        # query_serializer=BookSerializer,
        responses={
            '201': 'Book updated',
            '400': "Bad Request"
        },
        security=[],
        operation_id='Update_Book',
        operation_description='Update Book Name through isbn. Both id and isbn field should have same value.',
        )
    def put(self,request,pk):
        try:
            book=self.get_post(pk)
            serializer=BookSerializer(book,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response (serializer.data)
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            data={}
            data['message']='isbn does not match any book.'
            return Response(data)
        
    @swagger_auto_schema(
        operation_id='Delete_Book',
        operation_description='Delete book from the database. Id is isbn number of the book.',
        )
    def delete(self,request,pk):
        try:
            book=self.get_post(pk)
            book.delete()
            data={}
            data['status']='Deleted'
            return Response(data)
        except:
            data={}
            data['message']='isbn does not match any book.'
            return Response(data)
        
