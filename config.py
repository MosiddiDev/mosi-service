from flask import request, jsonify, Response, render_template, send_from_directory
from web import app
import requests
import time
import json
import urllib2


# @app.route("/config/<path:application>/<path:environment>", methods=['GET'])
# def public_config(application, environment):

# 	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'public.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/public.json'.format(app=application, env=environment)).read()

# @app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
# def private_config(application, environment):

# 	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'private.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/private.json'.format(app=application, env=environment)).read()

@app.route("/<regex('[_a-Z]*'):application>-<regex('[_a-Z]*'):environment>-<regex('[_a-Z]*'):config>", methods=['GET'])
def public_config(application, environment, config):

	# return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'public.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/public.json'.format(app=application, env=environment)).read()
	return '{app}, {env}, {con}'.format(app=application, env=environment, con=config)

@app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
def private_config(application, environment):

	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'private.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/private.json'.format(app=application, env=environment)).read()
	