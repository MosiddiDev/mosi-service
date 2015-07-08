import os
from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app)

from studentService import *

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
