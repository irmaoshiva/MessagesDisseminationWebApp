from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from management.models import Building, User, Messages
 
import requests

# Create your views here.

def home(request):
	return HttpResponse('<h1>Admin Home</h1>')

def buildings(request):
	if request.method == 'POST':
		_id = request.POST['id']
		_name = request.POST['name']
		print(_id)
		print(_name)
		#_lat = request.POST.get('lat')
		#_longit = request.POST.get('longit')
		building = Building(id = _id, name = _name)
		#uilding = Building(id = _id, name = _name, lat = _lat, longit = _longit)
		#aux = request.POST
		#building = Building(id = aux['id'], name = aux['name'], lat = aux['lat'], longit = aux['longit'])
		building.save()
		return HttpResponse('<h1>SHOW ALL BUILDINGS</h1>')
	else:
		buildings = Building.objects.all()	
		response = serialize("json", buildings)
		return HttpResponse(response, content_type = 'application/json')

def users(request):
	return HttpResponse('<h1>SHOW ALL USER</h1>')