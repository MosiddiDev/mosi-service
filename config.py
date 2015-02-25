from flask import request, jsonify, Response, render_template
from web import app
import requests
import time
import json
import urllib2


@app.route("/config/test", methods=['GET'])
def test_js():
	response_object = {
		'stat': 'ok',
		'test': []
	}

	return jsonify(response_object)

@app.route("/config/public.json", methods=['GET'])
def public_config(app='subscribe'):

	public_config = open('configs/{}/public.json'.format(app)).read()
	return public_config

@app.route("/config/private/.json", methods=['GET'])
def private_config(app='subscribe'):

	private_config = open('configs/{}/private.json'.format(app)).read()
	return private_config