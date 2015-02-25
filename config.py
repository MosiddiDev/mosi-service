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
	return send_from_directory('configs/subscribe/stage', 'public.json', as_attachment=True)

@app.route("/config/<path:environment>/<path:application>", methods=['GET'])
def public_config(environment, application):

	return send_from_directory('configs/{app}/{env}', 'public.json', as_attachment=True) if '.json' in application else open('configs/{app}/{env}/public.json'.format(env=environment, app=application)).read()

@app.route("/config/private/<path:environment>/<path:application>", methods=['GET'])
def private_config(environment, application):

	return send_from_directory('configs/{app}/{env}', 'private.json', as_attachment=True) if '.json' in application else open('configs/{app}/{env}/private.json'.format(env=environment, app=application)).read()