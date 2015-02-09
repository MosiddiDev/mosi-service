from flask import render_template, request
from web import app

@app.route("/gup/login/", defaults={'applicationId':42}, methods=['GET','POST'])
@app.route("/gup/login/<applicationId>", methods=['GET','POST'])
def gup_login(applicationId):
	return render_template('gupui-login-stub.html', applicationId=applicationId, postData=request.form)

@app.route("/gup/login-success/", defaults={'applicationId':42}, methods=['GET','POST'])
@app.route("/gup/login-success/<applicationId>", methods=['GET','POST'])
def gup_login_success(applicationId):
	return render_template('gup-stub-login-success.html', applicationId=applicationId, postData=request.form)
