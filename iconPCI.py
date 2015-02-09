import json
from flask import Flask, request, make_response, redirect
from web import app

@app.route('/icon/<method>', methods=['GET', 'POST'])
def icon(method):
	status = icon_getStatus()
	if icon_getRequest('redirectUrl'):
		return icon_getRedirectResponse(icon_getRequest('redirectUrl'), status)
	else:
		return icon_getJasonResponse(status)

def icon_getStatus():
	if icon_getRequest('forceStatus'):
		status = int( icon_getRequest('forceStatus'), 10 )
	else:
		status = icon_validateForm()
			
	return status

def icon_getRedirectResponse(redirectUrl, status):
	if '?' in redirectUrl:
		delimeter = '&'
	else:
		delimeter = '?'

	redirectUrl = redirectUrl+delimeter+'status='+str(status)
	return redirect( redirectUrl )

def icon_getJasonResponse(status):
	if request.args.get('callback'):
		responseStringTemplate = request.args.get('callback')+'(%s)'
	else:
		responseStringTemplate = '%s'
	
	responseObject = {
		'meta': {
			'status': status,
			'message': 'WARNING: We only use this for debugging so it is not stubbed out.'
		}
	}
	return make_response((responseStringTemplate % json.dumps(responseObject)), 200, {'Content-Type': 'application/json'})

def icon_getRequest(key):
	if request.args.get(key):
		return request.args.get(key)
	elif key in request.form:
		return request.form[key]
	else:
		return False

def icon_validateForm():
	return 0 # Don't bother validating this for now... it's just a stub.