from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Preferences
from .serializers import PreferencesSerializer

# Create and List Preferences
class CreatePreferences(APIView):
    def post(self, request):
        serializer = PreferencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        preferences = Preferences.objects.all()
        serializer = PreferencesSerializer(preferences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve, Update, or Delete Preferences by ID
class PreferencesDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        preference = get_object_or_404(Preferences, pk=pk)
        serializer = PreferencesSerializer(preference)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        preference = get_object_or_404(Preferences, pk=pk)
        serializer = PreferencesSerializer(preference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        preference = get_object_or_404(Preferences, pk=pk)
        preference.delete()
        return Response({"message": "Preferences deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
