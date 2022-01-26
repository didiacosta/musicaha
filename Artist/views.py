#import librerias externas
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
#librerias internas
from utilities.structure import Structure

#import modelos
from .models import Artist
#import serializers
from .serializers import ArtistSerializer

# Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
	"""
		Documentacion de mi recurso
	"""

	model = Artist
	serializer_class = ArtistSerializer
	queryset = model.objects.all()
	parser_classes = (FormParser, MultiPartParser,)
	paginate_by = 10

	#Devuelve 1 Artista recibe un id
	def retrieve(self,request,*args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		#return serializer.data
		#return {'status':'success', 'message':'', 'data':serializer.data}	
		return Response(Structure.success('',serializer.data),
			status=status.HTTP_200_OK)

	#Devuelve una lista de artistas, recibe dato	
	def list(self,request,*args, **kwargs):
		queryset = super(ArtistViewSet, self).get_queryset()

		dato = self.request.query_params.get('dato', None)
		qset = ~(Q(id=0))

		if dato:
			qset = qset & (Q(nickName__icontains=dato) | 
				Q(firstName__icontains=dato) | 
				Q(firstName__icontains=dato))

		queryset = self.model.objects.filter(qset).order_by('firstName','lastName')

		if queryset.count() == 0:
			message = 'No se encontraron datos'
		else:
			message = ''

		serializer = self.get_serializer(queryset, many=True)

		return Response(Structure.success(message,serializer.data),
			status=status.HTTP_200_OK)		




	#Crea un artista
	def create(self, request, *args, **kwargs):
		pass

	#Actualiza un artista	
	def update(self,request,*args,**kwargs):
		pass

	#destruye un artista	
	def destroy(self,request,*args,**kwargs):
		pass

