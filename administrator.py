import requests, json
from pprint import pprint

def login():
	print("Username:")
	username = input("> ")
	print("Password:")
	password = input("> ")

	payload = {"username" : username, "password" : password}
	r = requests.post("http://127.0.0.1:8000/admin/login/", data=payload)
	data = r.json()
	print(data)
	

def logout():
	r = requests.get("http://127.0.0.1:8000/admin/logout/")

def define_buildings():
	json_data = open('buildings-alameda.json')
	buildings_dict = json.load(json_data) #deserialises data
	buildings_dict = buildings_dict['containedSpaces']

	for aux in buildings_dict:
		pprint(aux)

		payload = {"id" : aux['id'], "name": aux['name'], "lat" : aux['lat'], "longit" : aux['longit']}
		r = requests.post("http://127.0.0.1:8000/admin/buildings/", data=payload)

def cenas():
	r = requests.get("http://127.0.0.1:8000/admin/users/")

def main():
	login()

	while True:
		print("Action:")
		print("(1) - Define builds and their locations (latitude, longitude)")
		print("(2) - List all users that are logged-in into the system")
		print("(3) - List all users that are inside a certain buiding")
		print("(4) - List the history of all the user movements and exchanged messages this list can be configured with a simple query to select the user or building")
		print("(5) - Logout")

		command = input('>> ')

		if command == '1':
			print("Tou aqui 1")
			cenas()
		elif command == '5':
			print("Tou aqui 5")
			logout()
	
if __name__ == "__main__":
    main()