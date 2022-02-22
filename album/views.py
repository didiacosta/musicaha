#import librerias externas
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
#librerias internas
from utilities.structure import Structure
from utilities.functions import Functions
#import modelos
from .models import Album
#import serializers
from .serializers import AlbumSerializer

# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
	"""
		Documentacion de mi recurso
	"""

	model = Album
	serializer_class = AlbumSerializer
	queryset = model.objects.all()
	parser_classes = (FormParser, MultiPartParser,)
	#paginate_by = 10

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
		queryset = super(AlbumViewSet, self).get_queryset()

		dato = self.request.query_params.get('dato', None)
		artist = self.request.query_params.get('artist', None)
		artistNick = self.request.query_params.get('artistnick', None)
		sinpaginacion = self.request.query_params.get('sinpaginacion', None)

		qset = ~(Q(id=0))

		if dato or artist or artistNick:
			if dato:
				qset = qset & (Q(name__icontains=dato))
			elif artist:
				qset = qset & (Q(artist__id=artist))
			else:
				qset = qset & (Q(artist__nickName__icontains=artistNick))

		queryset = self.model.objects.filter(qset).order_by('id')

		if queryset.count() == 0:
			message = 'No se encontraron datos'
		else:
			message = ''

		serializer = self.get_serializer(queryset, many=True)

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


	#Crea un album
	def create(self, request, *args, **kwargs):
		if request.method == 'POST':

			serializer = AlbumSerializer(
				data=request.data, context={'request': request})

			if serializer.is_valid():
				serializer.save(
					artist_id = request.data['artist_id'])

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

	#Actualiza un album	
	def update(self,request,*args,**kwargs):

		if request.method == 'PUT':
			partial = kwargs.pop('partial', False)
			instance = self.get_object()
			
			serializer = AlbumSerializer(
				instance, 
				data=request.data, 
				context={
					'request': request
				},
				partial=partial)

			if serializer.is_valid():
				serializer.save(
					artist_id=request.data['artist_id'])

				return Response(Structure.success(
					'El registro ha sido actualizado exitosamente',serializer.data),
					status = status.HTTP_200_OK)
			else:
				#import pdb; pdb.set_trace()
				return Response(Structure.error(
					'Datos requeridos no fueron recibidos'),
					status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(Structure.error(
				'Este servicio solo acepta peticiones PUT'),
				status=status.HTTP_400_BAD_REQUEST)


	#destruye un album	
	def destroy(self,request,*args,**kwargs):
		if request.method == 'DELETE':
			try:
				instance = self.get_object()
				if instance:
					self.perform_destroy(instance)
					return Response(Structure.success(
						'El registro ha sido eliminado correctamente',None),
						status = status.HTTP_200_OK)				
				else:
					return Response(Structure.error(
						'El album no fue encontrado'),
						status=status.HTTP_400_BAD_REQUEST)		

			except Exception as e: #capturo la excepción
				Functions.toLog(e,'album.views.destroy')
				return Response(Structure.error(
					'Se presentaron errores en el servidor, comuniquese con ' + \
					 'el administrador de sistema'),
					status=status.HTTP_500_INTERNAL_SERVER_ERROR)	

		else:
			return Response(Structure.error(
				'Este servicio solo acepta peticiones DELETE'),
				status=status.HTTP_400_BAD_REQUEST)

def home_view(request):
	username = request.user.username
	if request.user.is_authenticated:
		return render(request,'album/albumhome.html',{'username':username.capitalize()}) 
	else:
		return render(request,'usuario/login.html',{}) 


