from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests



def post_func():
	payload = {"id":1,"name":"Torre de Eletro","lat":38.7363775,"longit":-9.138574}
	r = requests.post("http://127.0.0.1:5000/admin/buildings", json=payload)
	payload1={"id" :2448131361155, "name" : "Pavilhão de Mecânica III","lat":38.7368263,"longit": -9.139276}
	r = requests.post("http://127.0.0.1:5000/admin/buildings", json=payload1)
	payload={"id" : "2448131361119","name" : "Pavilhão de Matemática","lat": 38.7358895,"long": -9.1399463}
	r = requests.post("http://127.0.0.1:5000/admin/buildings", json=payload)
	

post_func();

