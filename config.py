from flask import request, jsonify, Response, render_template
from web import app
import requests
import time
import json


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
