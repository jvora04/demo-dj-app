from crypt import methods
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import viewsets,generics,mixins, status

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Book
from .serializers import BookSerializer





# ---------------------------------------------------------
# MODEL VIEWSET
# ---------------------------------------------------------


class BookModelViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']


# ---------------------------------------------------------
# VIEWSET
# ---------------------------------------------------------
# class BookViewSet(viewsets.ViewSet):
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title']
    # filter_backends = [SearchFilter]
    # search_fields = ['title']

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     book = Book.objects.all()
    #     serializer = BookSerializer(book, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self, request):
    #     serializer = BookSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     book = Book.objects.get(pk=pk)
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data, status=status.HTTP_200_OK)




 
# ---------------------------------------------------------
# GENERIC API VIEWS
# ---------------------------------------------------------
# class GenericAPIView(generics.GenericAPIView, 
#     mixins.ListModelMixin, mixins.CreateModelMixin, 
#     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
#     mixins.DestroyModelMixin):

#     serializer_class = BookSerializer
#     queryset = Book.objects.all()

#     lookup_field = 'pk'

#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(pk)
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
#     def put(self, request, pk=None):
#         return self.update(request, pk)
    
#     def delete(self, request, pk=None):
#         return self.delete(request, pk);

# ---------------------------------------------------------
# CLASS BASED VIEWS
# ---------------------------------------------------------
# class book_list(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many = True)
#     filter_backends = [SearchFilter]
#     search_fields = ['author']
#     # pagination_class = PageNumberPagination

#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many = True)
#         # filter_backends = [SearchFilter]
#         # search_fields = ['title']
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class book_detail(APIView):    
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
#     def get(self,request,pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request,pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------
# FUNCTION BASED VIEWS
# ---------------------------------------------------------
# @csrf_exempt
# def book_list(request):
#     if request.method == 'GET':
#         book_list = Book.objects.all()
#         serializer = BookSerializer(book_list, many=True)
#         return JsonResponse(serializer.data, safe=False)        

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)

#         return JsonResponse(serializer.errors, status=400)
        

# @csrf_exempt
# def book_detail(request, pk):
    
#     try:
#         book_detail = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status=404)
    
        
    
#     if request.method == 'GET':
#         serializer = BookSerializer(book_detail)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(book_detail, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)

#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         book_detail.delete()
#         return HttpResponse(status = 200)