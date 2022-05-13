from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from usuario.models import AppUser
from rest_framework.response import Response
from rest_framework import status
from utilities.structure import Structure
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def login_view(request):

	mensaje = ''
	if request.user.is_authenticated:
		# Lo redirecciono al homepage de mi aplicacion
		return redirect(reverse('usuario.home'))
	else:
		if request.method == 'POST':
			username = request.POST.get('usuario')
			password = request.POST.get('password')
			#import pdb; pdb.set_trace()
			user = authenticate(username=username, password=password)

			if user:
				# el usuario existe, voy a ver si esta activo:
				if user.is_active:
					# redireccionar al homepage
					login(request, user)
					return redirect(reverse('usuario.home'))
				else:
					mensaje = 'el usuario ' + username + ' no se encuentra activo, ' + \
					'consulte con el administrador del sistema'

			else:
				# el usuario no existe
				mensaje = 'nombre de usuario y/o contraseña incorrectos'

	return render(request, 'usuario/login.html', {'mensaje': mensaje})

def logout_view(request):
	logout(request)
	return redirect(reverse('usuario.login'))

def home_view(request):
	username = request.user.username
	if request.user.is_authenticated:
		objUsuario = AppUser.objects.get(user__id=request.user.id)
		#import pdb; pdb.set_trace()
		return render(request,'usuario/home.html',
			{
				'username': username.capitalize(),
				'foto': settings.MEDIA_ROOT + '\\' +  \
				 objUsuario.foto.name.replace('/','\\')
			}
		) 
	else:
		return render(request,'usuario/login.html',{})

@csrf_exempt
def loginAppWeb(request):
	mensaje = ''

	if request.method == 'POST':
		username = request.POST.get('usuario')
		password = request.POST.get('password')
		#import pdb; pdb.set_trace()
		user = authenticate(username=username, password=password)
		if user:
			# el usuario existe, voy a ver si esta activo:
			if user.is_active:
				# redireccionar al homepage
				login(request, user)
				body = {'id' : user.appuser.id,
					'username': user.username,
					'foto': user.appuser.foto.name}
				status1 = 200
				

			else:
				mensaje = 'el usuario ' + username + ' no se encuentra activo, ' + \
				'consulte con el administrador del sistema'
				body = {'message': mensaje}
				status1 = 400
		else:
			# el usuario no existe
			mensaje = 'nombre de usuario y/o contraseña incorrectos'
			body = {'message': mensaje}
			status1 = 400

		#return Response(Structure.warning(mensaje),status = status.HTTP_400_BAD_REQUEST)
		#body = json.dumps(body)
		#response = HttpResponse(content=body, status=status)
		if status1 == 200:
			return JsonResponse(Structure.success('',body), status = status.HTTP_200_OK)
		else:
			return JsonResponse(Structure.warning(mensaje),status = status.HTTP_400_BAD_REQUEST)
		#return response
