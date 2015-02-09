from flask import request, jsonify, Response, render_template
from web import app
import requests
import time
import json


providers_map = {
	"aol": "AOL",
	"amazon": "Amazon",
	"facebook": "Facebook",
	"flickr": "Flickr",
	"myspace": "MySpace",
	"yahoo": "Yahoo!",
	"google": "Google",
	"googleplus": "Google+",
	"instagram": "Instagram",
	"linkedin": "LinkedIn",
	"twitter": "Twitter",
	"tumblr": "tumblr"
}


@app.route("/janrain/engage_js", methods=['GET'])
def engage_js():
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


@app.route("/janrain/get_available_providers", methods=['GET', 'POST'])
def get_available_providers():
	response_object = {
		'stat': 'ok',
		'signin': []
	}

	for key, value in providers_map.items():
		response_object['signin'].append(key)

	return jsonify(response_object)


@app.route("/janrain/auth_info", methods=['POST'])
def auth_info():
	return jsonify(json.loads(request.form.get('token')))


@app.route("/janrain/social-login", methods=['GET'])
def social_login():
	return render_template(
		'janrain-social-login.html',
		time=int(time.time()),
		request_parameters=dict(request.args),
		form_action=request.referrer or '/',
		social_provider=request.args.get('social-provider'),
		social_provider_name=providers_map.get(request.args.get('social-provider', ''), '')
	)
