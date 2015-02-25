from flask import Response, send_from_directory
from web import app


@app.route("/config/<path:application>/<path:environment>", methods=['GET'])
def public_config(application, environment):

	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'public.json', as_attachment=True) if '.json' in environment else Response(open('configs/{appname}/{env}/public.json'.format(appname=application, env=environment)).read(), headers={'content-type': 'application/json'})

@app.route("/config/private/<path:application>/<path:environment>", methods=['GET'])
def private_config(application, environment):

	return send_from_directory('configs/{app}/{env}'.format(app=application, env=environment.split('.')[0]), 'private.json', as_attachment=True) if '.json' in environment else Response(open('configs/{appname}/{env}/private.json'.format(appname=application, env=environment)).read(), headers={'content-type': 'application/json'})
