import requests, json
from pprint import pprint

def login():
	while True:
		print("Username:")
		username = input("> ")
		print("Password:")
		password = input("> ")

		payload = {"username" : username, "password" : password}
		r = requests.post("http://127.0.0.1:8000/admin/login/", data = payload)

		print('Status: ' + str(r.status_code) + '\n')

		if r.status_code == 401:
			print('Error: Invalid Login\n')
			main()
			return
		elif r.status_code != 200:
			print('Error Accessing\n')
			return

		print('Message: ' + r.text + '\n')

	secret = r.json()
	print('Secret: ' + str(secret['secret']) + '\n')

	return secret

def defineBuildings(secret):
	pprint(secret)

	json_data = open('buildings-alameda.json')
	buildings_dict = json.load(json_data) #deserialises data
	buildings_dict = buildings_dict['containedSpaces']

	for aux in buildings_dict:
		pprint(aux)

		payload = {"secret" : secret['secret'], "id" : aux['id'], "name": aux['name'], "lat" : aux['lat'], "longit" : aux['longit']}
		pprint(payload)
		r = requests.post("http://127.0.0.1:8000/admin/buildings/", data=payload)

		print('Status: ' + str(r.status_code) + '\n')
		print('Message: ' + r.text + '\n')

		if r.status_code == 401:
			print('Error: Invalid Login\n')
			main()
			return
		elif r.status_code != 200:
			print('Error Accessing\n')
			return

def allUsers(secret):
	i = 0
	pprint(secret)

	r = requests.post("http://127.0.0.1:8000/admin/users/", data = secret)

	print('Status: ' + str(r.status_code) + '\n')

	if r.status_code == 401:
		print('Error: Invalid Login\n')
		main()
		return
	elif r.status_code != 200:
		print('Error Accessing\n')
		return

	data = r.json()

	for aux in data:
		print("USER " + str(i))
		print('IST ID: ' + aux['pk'])
		print('Name: ' + aux['fields']['name'] + '\n')
		i = i + 1

def buildingUsers(secret):
	i = 0
	pprint(secret)

	print("Building ID:")
	build_id = input("> ")

	payload = {"secret" : secret['secret'], "build_id" : build_id}

	r = requests.post("http://127.0.0.1:8000/admin/building/users/", data = payload)

	print('Status: ' + str(r.status_code) + '\n')

	if r.status_code == 401:
		print('Error: Invalid Login\n')
		main()
		return
	elif r.status_code != 200:
		print('Error Accessing\n')
		return

	data = r.json()

	for aux in data:
		print("USER " + str(i))
		print('IST ID: ' + aux['pk'])
		print('Name: ' + aux['fields']['name'] + '\n')
		i = i + 1

def registerBot(secret):
	pprint(secret)

	print("Building ID:")
	build_id = input("> ")

	payload = {"secret" : secret['secret'], "build_id" : build_id}

	r = requests.post("http://127.0.0.1:8000/admin/bots/", data = payload)

	print('Status: ' + str(r.status_code) + '\n')

	if r.status_code == 401:
		print('Error: Invalid Login\n')
		main()
		return
	elif r.status_code != 200:
		print('Error Accessing\n')
		return

	data = r.json()

	print('Bot ID: ' + str(data['bot_id']))

def logout(secret):

	pprint(secret)
	r = requests.post("http://127.0.0.1:8000/admin/logout/", data = secret)

	print('Status: ' + str(r.status_code) + '\n')
	print('Message: ' + r.text + '\n')

	if r.status_code != 200:
		main()
		return

def main():
	print("\n---------- ADMINISTRATOR PAGE ----------\n")

	secret = login()

	while True:
		print("Action:")
		print("(1) - Define builds and their locations (latitude, longitude)")
		print("(2) - List all users that are logged-in into the system")
		print("(3) - List all users that are inside a certain buiding")
		print("(4) - List the history of all the user movements and exchanged messages this list can be configured with a simple query to select the user or building")
		print("(5) - Register a new bot")
		print("(6) - Logout")

		command = input('>> ')

		if command == '1':
			print('Tou aqui 1\n')
			defineBuildings(secret)

		elif command == '2':
			print('Tou aqui 2\n')			
			allUsers(secret)

		elif command == '3':
			print('Tou aqui 3\n')			
			buildingUsers(secret)

		elif command == '5':
			print('Tou aqui 5\n')			
			registerBot(secret)

		elif command == '6':
			print('Tou aqui 6\n')			
			logout(secret)

		else:
			print('Insert a valid command!\n')
	
if __name__ == "__main__":
    main()