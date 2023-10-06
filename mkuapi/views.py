from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Create your views here.
class StudentsViewSet(viewsets.ModelViewSet):
    # queryset = Student.objects.all()
    queryset = Student.objects.filter(is_active=True).order_by('-id')
    serializer_class = StudentSerializer
    permission_classes = [ permissions.AllowAny ] 
    pagination_class = CustomPageNumberPagination
    




    