from flask import Flask
from flask_restx import Api,Resource
import sys
import json

app = Flask(__name__)
api = Api(app)
port = 5000

# print("In File: run.py, Line: 10",sys.argv)
if sys.argv.__len__() > 1:
    port = sys.argv[1]

class HelloWorld(Resource):
    def get(self): 
        return json.dumps({"Message":"ok"})




# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


api.add_resource(HelloWorld,'/fo')
if __name__ == "__main__":
    app.run(port='5000',
            debug=app.config['DEBUG'], host="0.0.0.0")
