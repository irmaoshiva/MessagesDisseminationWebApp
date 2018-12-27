import requests, json
from pprint import pprint

def define_buildings():
	json_data = open('buildings-alameda.json')
	buildings_dict = json.load(json_data) #deserialises data
	buildings_dict = buildings_dict['containedSpaces']

	for aux in buildings_dict:
		pprint(aux)

		payload = {"id" : aux['id'], "name": aux['name'], "lat" : aux['lat'], "longit" : aux['longit']}
		r = requests.post("http://127.0.0.1:8000/admin/buildings/", data=payload)

define_buildings()
	
#if __name__ == "__main__":
#    main()