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
	#Deleting database
	Buildings.objects.all().delete()

	if request.method == 'POST':
		json_data = open('buildings-alameda.json')
		buildings_dict = json.load(json_data) #deserialises data
		buildings_dict = buildings_dict['containedSpaces']

		for aux in buildings_dict:
			pprint(aux)
			print(aux['id'])
			print(aux['name'])
			print(aux['lat'])
			print(aux['longit'])
			print("------------------------")

			_building = Buildings(id = aux['id'], name = aux['name'], lat = aux['lat'], longit = aux['longit'])
			_building.save()

		return HttpResponse('<h1>SHOW ALL BUILDINGS</h1>')
	else:
		buildings = Buildings.objects.all()	
		response = serialize("json", buildings)
		return HttpResponse(response, content_type = 'application/json')

def users(request):
	return HttpResponse('<h1>SHOW ALL USER</h1>')