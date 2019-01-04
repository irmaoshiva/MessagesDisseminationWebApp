import requests, json, random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.serializers import serialize

# para a cache
from django.utils.decorators import method_decorator
from django.core.cache import cache

from management.models import Buildings, Users, Messages

from pprint import pprint

# Create your views here.

def home(request):
	print('cheguei aqui?')
	return HttpResponse('<h1>TESTE</h1>')

def login_view(request):

	if request.method == 'POST':
		# Try to log user
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		print(username)
		print(password)

		if not username:
			print("lalalal")

		if not password:
			print("lalalal")

		secret = random.randint(1, 101)
		print(secret)

		while cache.get(secret, -1) != -1:
			secret = random.randint(1, 101)
			print(secret)

		user = authenticate(request, username = username, password = password)

		print('fiz autenticacao')

		if user is not None:
			print('fiz login')

			cache.set(secret, 1, 30)

			print(cache.get(secret, -1))

			return jsonify('Success in Login')

			#return redirect('admin:home')
		else:
			return 'Error in Login'
	else:
		return HttpResponse('<h1>Error: Invalid Method</h1>')

def logout_view(request):
	if request.method=='POST':
		secret = request.POST.get('secret', '')

		if not secret:
			return HttpResponse('<h1>ERROR 1/h1>')

		if cache.get(secret, -1) == -1:
			return HttpResponse('<h1>ERROR 2/h1>')

	#if request.user.is_authenticated:
	#	print('passei este if')
	print('Vou fazer logout')
	
	logout(request)
	return HttpResponse('<h1>Logout done</h1>')

#@login_required
#@login_required(login_url='admin:login_view')
def buildings(request):
	print("tou a vir aqui!!")

	if request.method == 'POST':
		aux = request.POST
		pprint(aux)
		_building = Buildings(id = aux['id'], name = aux['name'], lat = aux['lat'], longit = aux['longit'])
		_building.save()

		return HttpResponse('<h1>SHOW ALL BUILDINGS</h1>')
	else:
		_buildings = Buildings.objects.all()	
		response = serialize("json", _buildings)
		return HttpResponse(response, content_type = 'application/json')

#@login_required
def users(request):
	users_dict = Users.objects.all()
	pprint(users_dict)
	response = serialize("json", users_dict)
	return HttpResponse(response, content_type = 'application/json')

@login_required
def listUsersInBuilding(request, num):
	_users= Users.objects.filter(build_id=num)
	response = serialize("json", _users)	
	return HttpResponse(response, content_type = 'application/json')




def buildingsNum(request, num):
	_building=Buildings.objects.filter(id=num)
	response = serialize("json", _building)
	return HttpResponse(response, content_type = 'application/json')

def oneUser(request, ist_id):
	_user=Users.objects.filter(ist_id=ist_id)
	response = serialize("json", _user)
	return HttpResponse(response, content_type = 'application/json')


# from management.models import Buildings, Users
# Buildings.objects.all()
# build_x = Buildings.objects.get(name="Torre Norte")
# Users(ist_id = "ist425330", name = "Diogo Rodrigues", build_id = build_x, range_user = 100, lat = 38.7375584, longit = -9.1387255)
# Users.objects.all()
