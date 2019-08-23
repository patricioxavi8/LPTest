from .models import *


from rest_framework import serializers


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = curso
        fields = ('nombre','categoria','url','url_imagen')

class CursoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = curso2
        fields = ('nombre','url','url_imagen','institucion')