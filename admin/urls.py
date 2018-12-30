from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

app_name = 'admin'

urlpatterns = [
	path('', csrf_exempt(views.home), name = 'home'),
	path('login/', csrf_exempt(views.login_view), name = 'login_view'),
	path('logout/', csrf_exempt(views.logout_view), name = 'logout_view'),
    path('buildings/', csrf_exempt(views.buildings), name = 'buildings'),
    path('buildings/<int:num>/', csrf_exempt(views.buildingsNum), name = 'buildingsNum'),
    path('buildings/<int:num>/users/', csrf_exempt(views.listUsersInBuilding), name = 'buildingsNum'),
    path('users/', csrf_exempt(views.users), name = 'users'),
    path('users/<str:ist_id>/', csrf_exempt(views.oneUser), name = 'oneUser'),
]

