from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class SpellAPIView():
    
    # POST - Cadastrar dados na API
    def post(self, request):
        
        # Armazer os dados que estão em JSON
        spellJson=request.data
        
        # Transformando o Json em PYTHON
        spellSerialized = SpellSerializer(data=spellJson)
        
        #Vereificar se os dados estão corretos
        spellSerialized.is_valid(raise_exception=True)
        
        #Slavar os dados no nosso banco de dados 
        spellSerialized.save()
        
        #Retornar pro cliente o resultado da requisição
        return Response(status=201, data=spellSerialized.data)