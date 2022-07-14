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
from .models import Artist, Country
#import serializers
from .serializers import ArtistSerializer, CountrySerializer

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
		sinpaginacion = self.request.query_params.get('sinpaginacion', None)

		qset = ~(Q(id=0))

		if dato:
			qset = qset & (Q(nickName__icontains=dato) | 
				Q(firstName__icontains=dato) | 
				Q(lastName__icontains=dato))

		queryset = self.model.objects.filter(qset).order_by('firstName','lastName')

		if queryset.count() == 0:
			message = 'No se encontraron datos'
		else:
			message = ''

		if sinpaginacion is None:
			page = self.paginate_queryset(queryset)
			if page is not None:
				serializer = self.get_serializer(page,many=True)
				return self.get_paginated_response(
					Structure.success(message,serializer.data))
		else:
			serializer = self.get_serializer(queryset, many=True)	
			return Response(Structure.success(message,serializer.data),
				status=status.HTTP_200_OK)			
		





	#Crea un artista
	def create(self, request, *args, **kwargs):
		if request.method == 'POST':

			serializer = ArtistSerializer(data=request.data, context={'request': request})
			#import pdb; pdb.set_trace()
			if serializer.is_valid():
				serializer.save(
					country_id=request.data['country_id']
					)
				return Response(Structure.success('El registro ha sido guardado correctamente',
					serializer.data),
					status = status.HTTP_200_OK)
			else:
				#import pdb; pdb.set_trace()
				return Response(Structure.error(
					'datos requeridos no fueron recibidos'),
					status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(Structure.error(
				'Este servicio solo recibe peticiones POST'),
				status=status.HTTP_400_BAD_REQUEST)

	#Actualiza un artista	
	def update(self,request,*args,**kwargs):
		pass

	#destruye un artista	
	def destroy(self,request,*args,**kwargs):
		pass


class CountryViewSet(viewsets.ModelViewSet):
	"""
		Documentacion de mi recurso
	"""

	model = Country
	serializer_class = CountrySerializer
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
		queryset = super(CountryViewSet, self).get_queryset()

		dato = self.request.query_params.get('dato', None)
		sinpaginacion = self.request.query_params.get('sinpaginacion', None)

		qset = ~(Q(id=0))

		if dato:
			qset = qset & (Q(name__icontains=dato))

		queryset = self.model.objects.filter(qset).order_by('name')

		if queryset.count() == 0:
			message = 'No se encontraron datos'
		else:
			message = ''

		if sinpaginacion is None:
			page = self.paginate_queryset(queryset)
			if page is not None:
				serializer = self.get_serializer(page,many=True)
				return self.get_paginated_response(
					Structure.success(message,serializer.data))
		else:
			serializer = self.get_serializer(queryset, many=True)	
			return Response(Structure.success(message,serializer.data),
				status=status.HTTP_200_OK)			
		
