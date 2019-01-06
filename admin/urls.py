from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

app_name = 'admin'

urlpatterns = [
	path('login/', csrf_exempt(views.login_view), name = 'login_view'),
	path('logout/', csrf_exempt(views.logout_view), name = 'logout_view'),
    path('buildings/', csrf_exempt(views.buildings), name = 'buildings'),
    path('users/', csrf_exempt(views.users), name = 'users'),
    path('building/users/', csrf_exempt(views.listUsersInBuilding), name = 'users_building'),
    path('bots/', csrf_exempt(views.registerBot), name = 'register_bot'),
    path('bots/messages/', csrf_exempt(views.sendMessagesBot), name = 'send_messages_bot'),


    path('buildings/<int:num>/', csrf_exempt(views.buildingsNum), name = 'buildingsNum'),
    path('users/<str:ist_id>/', csrf_exempt(views.oneUser), name = 'oneUser'),
]

