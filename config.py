# from flask import send_from_directory
# from web import app


# @app.route("/config/<path:application>/<path:environment>", methods=['GET'])
# def public_config(application, environment):

# 	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'public.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/public.json'.format(app=application, env=environment)).read()

# @app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
# def private_config(application, environment):

# 	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'private.json', as_attachment=True) if '.json' in environment else open('configs/{app}/{env}/private.json'.format(app=application, env=environment)).read()

from flask import Response
from web import app


@app.route("/config/<path:application>/<path:environment>", methods=['GET'])
def public_config(application, environment):
	return Response(open('configs/{appname}/{env}/public.json'.format(appname=application, env=environment)).read(), headers={'content-type': 'application/json'})

@app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
def private_config(application, environment):
	return Response(open('configs/{appname}/{env}/private.json'.format(appname=application, env=environment)).read(), headers={'content-type': 'application/json'})
