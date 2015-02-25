import os
from flask import Flask

app = Flask(__name__)

class RegexConverter(BaseConverter):
        def __init__(self, url_map, *items):
                super(RegexConverter, self).__init__(url_map)
                self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

from iconPCI import *
from akamaiContent import *
from janrain import *
from gupuiStub import *
from gusDemo import *
from config import *

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)