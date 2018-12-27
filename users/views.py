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
from django.contrib.auth.models import User
import requests
from django.utils.timezone import now


# para a cache
from django.utils.decorators import method_decorator
from django.core.cache import cache




import json
import os
import string

from django.db import connection
from django.conf import settings
from django.utils import timezone


# é para tirar isto daqui pois vai para os cookies!




client_id ='1695915081465930'
redirect_uri = 'http://127.0.0.1:8000/app/auth/'
request_url = 'https://fenix.tecnico.ulisboa.pt/oauth/userdialog?client_id=' + client_id + '&redirect_uri=' + redirect_uri
secret= 'XXknAbAk2nTLFdYByKqjDXVC+k94NYc5t34EUGYAxD4qaWUB+aopdY2z/9j5oRvDoTJFpaHhg42dsQ+mf6Gesg=='


def index(request):
	return render(request, './login.html')



# def login(request):
#	_buildx=Buildings.objects.get(id=2448131361155)
#	print("olaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#	_user = Users(ist_id = 'ist000', name = 'pedro', build_id=_buildx, range_user=10,lat= -15.3888, longit=-40.777)
#	_user.save()
#	return HttpResponse('<h1>Login Page</h1>')


def auxiliar(request):
	access_token=request.COOKIES.get('token')
	print("access_token")
	print(access_token)
	x=cache.get(access_token,-1)
	print("ist id é")
	print(x)
	return HttpResponse('<p>FUNCAO AUXILIAR </p>')




def login(request):
	return redirect(request_url)



def auth(request):
	code = request.GET.get('code')
	access_token_request_url = 'https://fenix.tecnico.ulisboa.pt/oauth/access_token'
	_data = {'client_id': client_id, 'client_secret': secret,'redirect_uri': redirect_uri, 'code': code, 'grant_type': 'authorization_code'}
	
	request_access_token = requests.post(access_token_request_url, data=_data)


	if request_access_token.status_code != 200 or 'error' in request_access_token.json():
		return render(request, './invalid.html')
	else:
		access_token = request_access_token.json().get('access_token')
		print("acess_token no login")
		print(access_token)
		refresh_token = request_access_token.json().get('refresh_token')
		token_expires = request_access_token.json().get('expires_in')

		params = {'access_token': access_token}
		request_info = requests.get('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/person', params=params)
		_ist_id = request_info.json().get('username')
		_name = request_info.json().get('name')

		y=cache.set(access_token,_ist_id,60*5)
		

		nr={}
		nr['ist_id']=_ist_id
		nr['name']=_name
		context ={'user':nr}
		if not Users.objects.filter(ist_id =_ist_id).exists():
			_user= Users(ist_id = _ist_id, name= _name, build_id='1', range_user = 100, lat=38.7368263, longit= -9.1392)
			_user.save()

		response = render(request, './userInterface.html',context)
		response.set_cookie('token', access_token)
		return response

def logout(request):
	# é para retirar isto:
	access_token=request.COOKIES.get('token')
	ist_id=cache.get(access_token,-1)
	if request.method=='POST':
		cache.delete('token')
		if request.COOKIES.get('token'):
			response = HttpResponse('Cookies cleared')
			response.delete_cookie('token')
		Users.objects.filter(ist_id=ist_id).delete()
		print('dentro do logout-> a cache é')
		print(cache.get('id'))
		return render(request, './GoodBye.html')



def range(request):
	if request.method == 'POST':
		# e para ir buscar a var. sessao
		access_token=request.COOKIES.get('token')
		ist_id=cache.get(access_token,-1)
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


def nearbyRange(request):
	access_token=request.COOKIES.get('token')
	ist_id=cache.get(access_token,-1)
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
	


def nearbyBuilding(request):
	access_token=request.COOKIES.get('token')
	ist_id=cache.get(access_token,-1)
	_me=Users.objects.filter(ist_id=ist_id)
	for aux in _me:
		print(aux.build_id)
		_users=Users.objects.filter(build_id=aux.build_id).filter(~Q(ist_id=ist_id))
	response = serialize("json", _users)
	return HttpResponse(response, content_type = 'application/json')
	

# @login_required(login_url='users:home')
def sendMessage(request):
	access_token=request.COOKIES.get('token')
	ist_id=cache.get(access_token,-1)
	if request.method == 'POST':
		_content=request.POST.get('message', '')
		_data= Users.objects.filter(ist_id=ist_id)
		for aux in _data:
			_range=aux.range_user
			_lat=aux.lat
			_longit=aux.longit
	# Q is to exclude the user with this ist_id
		_allUsers=Users.objects.all().filter(~Q(ist_id=ist_id))

		for item in _allUsers:
			if checkDistance(item.lat,_lat,item.longit,_longit,_range)==1:
				_message=Messages(content=_content,receiver=item,date=now())
				_message.save()
			
	allMessages=Messages.objects.all()
	response = serialize("json", allMessages)
	return HttpResponse(response, content_type = 'application/json')


# ESTE NÃO ESTÁ TESTADO!!!
def sendMessageBuild(request):
	access_token=request.COOKIES.get('token')
	ist_id=cache.get(access_token,-1)
	if request.method == 'POST':
		_content=request.POST.get('message', '')
		_data= Users.objects.filter(ist_id=ist_id)
		for aux in _data:
			_build_id=aux.build_id
			
	# Q is to exclude the user with this ist_id
		_allUsers=Users.objects.all().filter(~Q(ist_id=ist_id))

		for item in _allUsers:
			if item.build_id==_build_id:
				_message=Messages(content=_content,receiver=item,date=now())
				_message.save()
			
	allMessages=Messages.objects.all()
	response = serialize("json", allMessages)
	return HttpResponse(response, content_type = 'application/json')


# nao testado
def checkBuilding(_latUser,_longitUser):
	#verificar qual o raio a meter
	radius=2
	allBuilds=Buildings.objects.all()
	for item in allBuilds:
		if checkDistance(_latUser,item.lat,_longitUser,item.longit,radius)==1:
			return _build_id
	return -1
	

#nao bem testado pcausa do ajax
def updateLocation(request):
	if request.method =='POST':
		print('recebi um POST NO updateLocation')
		_lat=request.POST.get('lat')
		_longit=request.POST.get('longit')
		print("latitudee")
		print(_lat)
		print("longit")
		print(_longit)
		access_token=request.COOKIES.get('token')
		_ist_id=cache.get(access_token,-1)
		_build_id = checkBuilding(_lat,_longit)
		Users.objects.filter(ist_id=_ist_id).update(lat = _lat, longit = _longit, build_id= _build_id)

		return HttpResponse('<p>nadaa</p>')		





# def login(request):
#	_buildx=Buildings.objects.get(id=2448131361155)
#	print("olaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#	_user = Users(ist_id = 'ist000', name = 'pedro', build_id=_buildx, range_user=10,lat= -15.3888, longit=-40.777)
#	_user.save()
#	return HttpResponse('<h1>Login Page</h1>')




