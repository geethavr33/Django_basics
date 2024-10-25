from django.shortcuts import render
from rest_framework import generics
from .models import School
from .serializers import SchoolSerializer

class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer