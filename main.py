from flask import Flask, request
from flasgger import Swagger
from flasgger import swag_from
import json

app = Flask(__name__)


swagger = Swagger(app)

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello Paul!!!"

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/hello_world")
def hi():
    return "!!!"

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/json")
def summary():
    with open("hello_world.json", 'r') as file:
        data = json.load(file)
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
