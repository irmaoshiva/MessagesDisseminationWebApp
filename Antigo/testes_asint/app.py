from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
import json
from flask import request
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'ist425412'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pxfi3850'
app.config['MYSQL_DATABASE_DB'] = 'ist425412'
app.config['MYSQL_DATABASE_HOST'] = 'db.tecnico.ulisboa.pt'
mysql = MySQL(app)

mysql.init_app(app)



app = Flask(__name__)

@app.route('/admin/buildings',methods=['POST'])
def AddBuilding():
	if request.method == 'POST':
		aux=request.get_json()
		conn = mysql.connect()
		mycursor=conn.cursor()
		mycursor.execute('''INSERT INTO building VALUES("%d","%s","%f","%f")''' %(aux['id'],aux['name'],aux['lat'],aux['longit']))
		conn.commit()

@app.route('/admin/users/<id>',methods=['GET'])
def listCertainUsers(id):
	cur = mysql.connect().cursor()
	cur.execute('''select * from users where istid= "%s"'''%(id))

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)

@app.route('/admin/users/',methods=['GET'])
def listAllUsers():
	cur = mysql.connect().cursor()
	cur.execute('''select * from users ''')

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)

@app.route('/admin/buildings/<id>/users',methods=['GET'])
def listUserInBuilding(id):
	cur = mysql.connect().cursor()
	cur.execute('''select users.name, users.istid from users inner join building on users.build_id=building.id where building.id="%d" ''' %(int(id)))

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)


@app.route('/users/<id>/nearby/building/',methods=['GET'])
def seeNearbyInBuilding(id):
	cur = mysql.connect().cursor()
	cur.execute('''select users.name, users.istid from users inner join building on users.build_id=building.id where users.build_id in(select u.build_id from users as u where u.istid="%s")'''%(id))

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)

@app.route('/users/<id>/range',methods=['POST'])
def changeRange(id):
	aux=request.get_json()
	cur = mysql.connect().cursor()
	cur.execute(''' update users set range="%d",istid=istid where istid="%s"'''%(aux['user_range'],id))



def distance(_lat1,_lat2,_long1,_long2,_range):
	R = 6373.0

	lat1 = radians(_lat1)
	lon1 = radians(_long1)
	lat2 = radians(_lat2)
	lon2 = radians(_long2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	_distance = R * c*1000
	if _distance <_range:
		return 1
	return 0




@app.route('/users/<id>/nearby/range',methods=['GET'])
def seeNearbyinRange(id):
	cur = mysql.connect().cursor()
	cur.execute(''' select range_user,lat, longit from users where istid="%s" '''%(id))
	##trocar para fetch
	data=cur.fetchall()
	for row in data:
		range_u=row[0]
		lat=row[1]
		longit=row[2]


	cur.execute(''' select istid, lat,longit from users ''')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	users=[]
	for item in r:
		print('xauuuu')
		print(item['lat'])
		if distance(item['lat'],lat,item['longit'],longit,range_u)==1:
			print('olaaa')
			users.append(item['istid'])

	return str(users)
	






if __name__ == '__main__':
	app.run(debug = True)








