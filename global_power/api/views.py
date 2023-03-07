from django.shortcuts import render, get_object_or_404
from .serializers import PoderGlobalSerializer
from rest_framework import viewsets, permissions
from .models import PoderGlobal
from rest_framework.response import Response

# Create your views here.


# class PoderGlobalViewSet(viewsets.ModelViewSet):
#     queryset = PoderGlobal.objects.all()
#     serializer_class = PoderGlobalSerializer
#     #permission_classes = [permissions.IsAuthenticated]

class PoderGlobalViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PoderGlobal.objects.all()
        serializer = PoderGlobalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PoderGlobal.objects.all()
        poder_global = get_object_or_404(queryset, pk = pk)
        serializer = PoderGlobalSerializer(poder_global)
        return Response(serializer.data)