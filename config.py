from flask import request, jsonify, Response, render_template
from web import app
import requests
import time
import json
import urllib2


@app.route("/config/test", methods=['GET'])
def test_js():
	return Response("""window.janrain.engage = {
	'signin': {
		'url': window.janrain.settings.appUrl+'/social-login',
		'appendTokenParams': function(currentURLParameters){
			var glue = (this.url.indexOf('?') !== -1)? '&' : '?';
			for(key in currentURLParameters){
				this.url += glue+key+'='+encodeURIComponent(currentURLParameters[key]);
				glue = '&';
			}
		},
		'triggerFlow': function(socialLoginType){
			var glue = (this.url.indexOf('?') !== -1)? '&' : '?';
			this.url += glue+'social-provider='+encodeURIComponent(socialLoginType)
			location.href=this.url;
		}
	}
};""", headers={'content-type': 'text/javascript'})


@app.route("/config/test2", methods=['GET'])
def test2_js():
	response_object = {
		'stat': 'ok',
		'signin': []
	}

	return jsonify(response_object)

@app.route("/config/test3", methods=['GET'])
def test3_js():


	return '{\n  "signin": [], \n  "stat": "ok"\n}'

@app.route("/config/test4", methods=['GET'])
def test4_js():
	
	# try:
	# 	return urllib2.urlopen(config_location).read()

	try:
		with open('configs/subscribe/public.json') as public_config:
			return public_config
	except:		
		return '{\n  "default": [], \n  "it_was": "not_ok"\n}'