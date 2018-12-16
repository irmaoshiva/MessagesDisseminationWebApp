from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from management.models import Buildings, Users, Messages
from math import sin, cos, sqrt, atan2, radians
from django.db.models import Count, Q
import fenixedu
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import requests


import json
import os
import string

from django.db import connection
from django.conf import settings
from django.utils import timezone


# Create your views here.


config = fenixedu.FenixEduConfiguration \
	('1695915081465930', 'http://127.0.0.1:8000/app/auth/', 
		'XXknAbAk2nTLFdYByKqjDXVC+k94NYc5t34EUGYAxD4qaWUB+aopdY2z/9j5oRvDoTJFpaHhg42dsQ+mf6Gesg==',
		'https://fenix.tecnico.ulisboa.pt/')



client = fenixedu.FenixEduClient(config)



def index(request):
	context = {'auth_url': client.get_authentication_url()}
	return render(request, './login.html', context)



# def login(request):
#	_buildx=Buildings.objects.get(id=2448131361155)
#	print("olaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#	_user = Users(ist_id = 'ist000', name = 'pedro', build_id=_buildx, range_user=10,lat= -15.3888, longit=-40.777)
#	_user.save()
#	return HttpResponse('<h1>Login Page</h1>')


def auth(request):
	global client
	print("iiiiiiiiiiiiiiiiiiiiiiiiiiii")
	code = request.GET.get('code', None)
	print('o codigo e...')
	print(code)
	if code is not None and not request.user.is_authenticated:
		print('xxxxxxxxxxx')
		user = authenticate(request=request, client=client, code=code)
		print('yyyyyyyyyyyyyyyyyy')
		if user is not None:
			login(request, user)
	print("ooooooooooooooooooooooooooooooooooo")



def range(request,ist_id):
	if request.method == 'POST':
		_range= request.POST.get('range', '')
		Users.objects.filter(ist_id=ist_id).update(range_user = _range)
		return HttpResponse('<h1>oii/h1>')


def checkDistance(_lat1,_lat2,_long1,_long2,_range):
	R = 6373.0

	lat1 = radians(_lat1)
	lon1 = radians(_long1)
	lat2 = radians(_lat2)
	lon2 = radians(_long2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	_distance = R * c*1000
	if _distance <_range:
		return 1
	return 0


def nearbyRange(request,ist_id):
	_data= Users.objects.filter(ist_id=ist_id)
	for aux in _data:
		_range=aux.range_user
		_lat=aux.lat
		_longit=aux.longit
	# Q is to exclude the user with this ist_id
	_allUsers=Users.objects.all().filter(~Q(ist_id=ist_id))

	nearMe=[]
	for item in _allUsers:
		if checkDistance(item.lat,_lat,item.longit,_longit,_range)==1:
			print(item.ist_id)
			nearMe.append(item.ist_id)
			print('laaakjlkjlkjl')	

	print(nearMe)
	return HttpResponse('<p>olaa</p>')
	


def nearbyBuilding(request, ist_id):
	_me=Users.objects.filter(ist_id=ist_id)
	for aux in _me:
		print(aux.build_id)
		_users=Users.objects.filter(build_id=aux.build_id).filter(~Q(ist_id=ist_id))
	response = serialize("json", _users)
	return HttpResponse(response, content_type = 'application/json')
	






