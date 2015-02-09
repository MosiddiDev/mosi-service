from flask import Flask, request, make_response
from web import app

#Configs
akamai_config = {
	'fireflyEnabled': True,
	'fireflyThreshold': 20,
	'fireflyThresholdRegistered': 30,
	'anonymousURLProccessor': 'http://accountsolution-dev2.indystar.com/akamai/cookie/',
	'meterLimitURL': 'http://safe-dusk-4529.herokuapp.com/akamai/get-access'
}


@app.route('/akamai/ajax', methods=['GET'])
def akamai_ajax( ):
	return make_response('<h1>Get Access</h1><p>You should only be on this page if you have reached your meter limit.</p>', 200, {'Content-Type':'text/html'})


@app.route('/akamai/get-access', methods=['GET'])
def akamai_getAccess( ):
	return make_response('<h1>Get Access</h1><p>You should only be on this page if you have reached your meter limit.</p>', 200, {'Content-Type':'text/html'})


@app.route('/akamai/<scenario>/<contentKey>', methods=['GET'])
def akamai_content( scenario, contentKey ):
	if scenario == 'premium':
		response = akamai_scenarioPremiumOnly( contentKey )
	elif scenario == 'free':
		response = akamai_scenarioFree( contentKey )
	else:
		response = akamai_scenarioDefault( contentKey )

	return response


def akamai_scenarioDefault( contentKey ):
	headers = akamai_getHeader( contentKey, {
		'X-Content-Access-Type': 'Metered'
	})

	data = akamai_buildResponseData({
		'scenarioName': 'Metered',
		'scenarioDescription': 'This content is metered and should increment the user\'s count once (assuming they do not have market/product access).',
		'contentKey': contentKey,
		'headers': headers
	})

	return make_response(data, 200, headers)


def akamai_scenarioFree( contentKey ):
	headers = akamai_getHeader( contentKey, {
		'X-Content-Access-Type': 'Free'
	})

	data = akamai_buildResponseData({
		'scenarioName': 'Free',
		'scenarioDescription': 'This content should always be accessible and never increment the count.',
		'contentKey': contentKey,
		'headers': headers
	})

	return make_response(data, 200, headers)


def akamai_scenarioPremiumOnly( contentKey ):
	headers = akamai_getHeader( contentKey, {
		'X-Content-Access-Type': 'Premium-Only'
	})

	data = akamai_buildResponseData({
		'scenarioName': 'Premium Only',
		'scenarioDescription': 'This content should only be accessible by users with market/product access.',
		'contentKey': contentKey,
		'headers': headers
	})

	return make_response(data, 200, headers)


def akamai_getHeader( contentKey, additionalHeaders=False ):
	if additionalHeaders:
		headers = additionalHeaders
	else:
		headers = {}

	headers['Content-Type'] = 'text/html'
	headers['X-Content-Key'] = contentKey
	headers['X-Meter-Threshold'] = str(akamai_config['fireflyThreshold'])
	headers['X-Meter-Registered-Threshold'] = str(akamai_config['fireflyThresholdRegistered'])
	headers['X-Meter-Limit-URL'] = akamai_config['meterLimitURL']
	headers['X-Process-Anonymous-URL'] = akamai_config['anonymousURLProccessor']

	if akamai_config['fireflyEnabled']:
		headers['X-Meter-Enabled'] = 'Yes'

	return headers


def akamai_buildResponseData( context ):
	data =	'<h1>'+context['scenarioName']+'</h1>'
	data +=	'<p>'+context['scenarioDescription']+'</p>'
	data +=	'<h2>Headers</h2><ul>'
	for key, value in iter(sorted(context['headers'].iteritems())):
		data +=	'<li>'+key+': '+value+'</li>'
	data +=	'</ul>'

	return data