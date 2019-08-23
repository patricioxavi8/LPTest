from django.shortcuts import render

from . import models
from . import serializers
from rest_framework import generics



class CursosView(generics.ListAPIView):
    queryset = models.curso.objects.all()
    serializer_class = serializers.CursoSerializer

class CursosView2(generics.ListAPIView):
    queryset = models.curso2.objects.all()
    serializer_class = serializers.CursoSerializer2


class CreateCursosView(generics.CreateAPIView):
    queryset = models.curso.objects.all()
    serializer_class = serializers.CursoSerializer

class CursosViewFilter(generics.ListAPIView):
    serializer_class = serializers.CursoSerializer
    
    
    def get_queryset(self):
        filtro = self.kwargs['filtro']
        queryset = models.curso.objects.filter(nombre__contains=filtro)
        return  queryset
    