from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import MasterCode
from .serializers import MasterCodeSerializer

class IsAdminUserMixin:
    """
    Mixin to check if the requesting user is an admin.
    """
    def is_admin(self, request):
        return request.user.is_staff or request.user.is_superuser


class MasterCodeListView(APIView, IsAdminUserMixin):
    """
    List all MasterCode entries or create a new one.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        master_codes = MasterCode.objects.all()
        serializer = MasterCodeSerializer(master_codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not self.is_admin(request):
            return Response(
                {"error": "Only admins can create data."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = MasterCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterCodeDetailView(APIView, IsAdminUserMixin):
    """
    Retrieve, update, or delete a MasterCode entry.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return MasterCode.objects.get(pk=pk)
        except MasterCode.DoesNotExist:
            return None

    def get(self, request, pk):
        master_code = self.get_object(pk)
        if not master_code:
            return Response(
                {"error": "MasterCode not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MasterCodeSerializer(master_code)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if not self.is_admin(request):
            return Response(
                {"error": "Only admins can update data."},
                status=status.HTTP_403_FORBIDDEN,
            )
        master_code = self.get_object(pk)
        if not master_code:
            return Response(
                {"error": "MasterCode not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MasterCodeSerializer(master_code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not self.is_admin(request):
            return Response(
                {"error": "Only admins can delete data."},
                status=status.HTTP_403_FORBIDDEN,
            )
        master_code = self.get_object(pk)
        if not master_code:
            return Response(
                {"error": "MasterCode not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        master_code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


