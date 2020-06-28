from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hola(Resource):
    def get(self):
        return {"Hola Mundo Cruel":"Creaste tu primer RESTful, o no.."}

api.add_resource(Hola, '/hola')

if __name__ == '__main__':
     app.run(debug=True)