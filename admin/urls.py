from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('', csrf_exempt(views.home), name = 'home'),
    path('buildings/', csrf_exempt(views.buildings), name = 'buildings'),
    path('users/', csrf_exempt(views.users), name = 'users'),
]