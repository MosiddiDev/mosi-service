from flask import request
from web import app
from dbConnect import DBConnect
import json


##########################
#### GET ALL STUDENTS ####
##########################
@app.route('/studentService/', methods=['GET'])
def get_students():
	db = DBConnect()
	result = db.query("SELECT * FROM students")
	db.close()

	return json.dumps(result)


#########################
#### GET ONE STUDENT ####
#########################
@app.route('/studentService/<id>', methods=['GET'])
def get_student(id):
	db = DBConnect()
	result = db.query("SELECT * FROM students WHERE id='{}'".format(id))
	db.close()

	return json.dumps(result)


########################
#### CREATE STUDENT ####
########################
@app.route('/studentService/', methods=['POST'])
def add_student():
	request_data = get_request_data(request)

	if len(request_data) == 0:
		return json.dumps({'error': 'no data'})

	db = DBConnect()

	values = (
		request_data.get('name'),
		request_data.get('phone'),
		request_data.get('email'),
		request_data.get('address'),
	)
	result = db.execute("INSERT INTO students (name, phone, email, address) VALUES (%s,%s,%s,%s)", values)
	response_object = {'method': 'created {}'.format(id)}
	db.close()

	return json.dumps(response_object)


########################
#### UPDATE STUDENT ####
########################
@app.route('/studentService/<id>', methods=['POST'])
def update_student(id):
	request_data = get_request_data(request)

	if len(request_data) == 0:
		return json.dumps({'error': 'no data'})

	db = DBConnect()

	result = db.execute("UPDATE students SET {} WHERE id='{}'".format(to_string(request_data), id))
	response_object = {'method': 'updated {}'.format(id)}
	db.close()

	return json.dumps(response_object)

def to_string(dic):
	"""
		This formats a dictionary as a string like so: 'KEY=VALUE' with kv pairs delimited by commas
	"""
	arr = []
	for key, value in dic.iteritems():
		arr.append('{}=\'{}\''.format(key, value))
	return ', '.join(arr)


########################
#### DELETE STUDENT ####
########################
@app.route('/studentService/<id>', methods=['DELETE'])
def delete_student(id):
	db = DBConnect()
	result = db.execute("DELETE FROM students WHERE id='{}'".format(id))
	response_object = {'method': 'deleted {}'.format(id)}
	db.close()

	return json.dumps(response_object)


def get_request_data(request):
	"""
		This should have been provided by Flask, but for some reason they
		completely separate 'request parameters' and 'content body', as a service
		I don't care, I just want the data the user sends so I 'attempt' to resolve it.
	"""
	try:
		request_data = json.loads(request.data)
	except:
		request_data = {}
	
	request_data.update(toDict(request.values))

	return request_data

def toDict(dict_type_object):
	"""
		Seemingly completely unnecessary but all these dict types (request.args)
		are formatted funny in their raw data, so I created this function to cut
		the BS and get a true dictionary (specifically where the value is not an
		array but just a string)
	"""
	true_dict = {}
	for key, value in dict_type_object.iteritems():
		true_dict[key] = value
	return true_dict

