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

@app.route("/config/<path:application>/<path:environment>", methods=['GET'])
def public_config(environment, application):

	return send_from_directory('configs/{app}/{env}'.format(env=environment, app=application.split('.')[0]), 'public.json', as_attachment=True) if '.json' in application else open('configs/{app}/{env}/public.json'.format(env=environment, app=application)).read()

@app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
def private_config(environment, application):

	return send_from_directory('configs/{app}/{env}'.format(env=environment, app=application.split('.')[0]), 'private.json', as_attachment=True) if '.json' in application else open('configs/{app}/{env}/private.json'.format(env=environment, app=application)).read()