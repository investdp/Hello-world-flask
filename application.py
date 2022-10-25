from flask import *

application = Flask(__name__)

@application.route('/')
def test():
    return 'helloworlds'
