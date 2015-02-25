from flask import request, jsonify, Response, render_template, send_from_directory
from web import app
import requests
import time
import json
import urllib2


@app.route("/config/test.json", methods=['GET'])
def test_js():
	response_object = {
		'stat': 'ok',
		'test': []
	}

	# return jsonify(response_object)
	return send_from_directory('configs', 'test.json', as_attachment=True)

@app.route("/config/public/<path:application>", methods=['GET'])
def public_config(application):

	public_config = open('configs/{}/public.json'.format(application)).read()
	return public_config

@app.route("/config/private/<path:application>", methods=['GET'])
def private_config(application):

	private_config = open('configs/{}/private.json'.format(application)).read()
	return private_config