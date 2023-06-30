from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import Curso

def index(request):
    context = {
        'status': True,
        'content': 'mi primer api en Django'
    }
    
    return JsonResponse(context)

def curso(request):
    listado_cursos = Curso.objects.all()
    
    context = {
        'status': True,
        'content': list(listado_cursos.values())
    }
    
    return JsonResponse(context)

@csrf_exempt
def post_curso(request):
    json_data = json.loads(request.body)
    
    titulo = json_data['titulo']
    description = json_data['description']
    imagen = json_data['imagen']
    
    nuevo_curso = Curso.objects.create(
        titulo=titulo,
        description=description,
        imagen=imagen
    )
    
    context = {
        'status': True,
        'content': f'Curso creado con el id {nuevo_curso.id}'
    }
    
    return JsonResponse(context)

""" uso de DRF"""
from rest_framework import generics
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer