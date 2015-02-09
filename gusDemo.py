from flask import request, jsonify, Response, render_template, url_for, send_from_directory
from web import app
import requests
import json


@app.route("/gus/gus-demo/<trylibrary>")
def gus_demo(trylibrary):
    trylibrary = trylibrary + '.html'
    return render_template(
        'gusDemos/'+trylibrary
    )
