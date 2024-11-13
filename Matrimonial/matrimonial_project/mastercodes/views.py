# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MasterCode
from .serializers import MasterCodeSerializer

class MasterCodeListView(APIView):
    """
    List all MasterCode entries or create a new one.
    """
    def get(self, request):
        master_codes = MasterCode.objects.all()
        serializer = MasterCodeSerializer(master_codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MasterCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MasterCodeDetailView(APIView):
    """
    Retrieve, update, or delete a MasterCode entry.
    """
    def get_object(self, pk):
        try:
            return MasterCode.objects.get(pk=pk)
        except MasterCode.DoesNotExist:
            return None

    def get(self, request, pk):
        master_code = self.get_object(pk)
        if not master_code:
            return Response({'error': 'MasterCode not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MasterCodeSerializer(master_code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        master_code = self.get_object(pk)
        if not master_code:
            return Response({'error': 'MasterCode not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MasterCodeSerializer(master_code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        master_code = self.get_object(pk)
        if not master_code:
            return Response({'error': 'MasterCode not found'}, status=status.HTTP_404_NOT_FOUND)
        master_code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
