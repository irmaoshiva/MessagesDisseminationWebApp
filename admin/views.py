from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from management.models import Buildings, Users, Messages
 
import requests, json
from pprint import pprint

# Create your views here.

def home(request):
	return HttpResponse('<h1>Admin Home</h1>')

def buildings(request):
	if request.method == 'POST':
		#Deleting database
		Buildings.objects.all().delete()

		json_data = open('buildings-alameda.json')
		buildings_dict = json.load(json_data) #deserialises data
		buildings_dict = buildings_dict['containedSpaces']

		for aux in buildings_dict:
			pprint(aux)

			_building = Buildings(id = aux['id'], name = aux['name'], lat = aux['lat'], longit = aux['longit'])
			_building.save()

		return HttpResponse('<h1>SHOW ALL BUILDINGS</h1>')
	else:
		_buildings = Buildings.objects.all()	
		response = serialize("json", _buildings)
		return HttpResponse(response, content_type = 'application/json')

def users(request):
	users_dict = Users.objects.all()
	
	for aux in users_dict:
		print("IST ID:")
		print(aux[])
		aux = aux['fields']


	return HttpResponse('<h1>SHOW ALL USER</h1>')


# from management.models import Buildings, Users
# Buildings.objects.all()
# build_x = Buildings.objects.get(name="Torre Norte")
# Users(ist_id = "ist425330", name = "Diogo Rodrigues", build_id = build_x, range_user = 100, lat = 38.7375584, longit = -9.1387255)
# Users.objects.all()
