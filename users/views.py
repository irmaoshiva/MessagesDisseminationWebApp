from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from management.models import Buildings, Users, Messages
 
import requests

# Create your views here.

def login(request):
	return HttpResponse('<h1>Login Page</h1>')

def home(request):
	return HttpResponse('<h1>User Home</h1>')


	#path('<str:ist_id>/', csrf_exempt(views.home), name = 'home'),
	#path('<str:ist_id>/messages/', csrf_exempt(views.messages), name = 'messages'),
    #path('<str:ist_id>/range/', csrf_exempt(views.range), name = 'range'),
    #path('<str:ist_id>/nearby/range/', csrf_exempt(views.nearbyRange), name = 'nearbyRange'),
    #path('<str:ist_id>/nearby/building/', csrf_exempt(views.nearbyBuilding), name = 'nearbyBuilding'),