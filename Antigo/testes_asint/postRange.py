from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests



def post_func():
	payload = {"range":13}
	r = requests.post("http://127.0.0.1:8000/app/ist425412/range/", data=payload)

post_func();