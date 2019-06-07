from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from filter import Filter

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def get(self):
        query = request.args
        f = Filter()
        f.ParseArgs(query)
        result = {'keywords': f.keywords, 'min_salary': f.min_salary}
        return jsonify(result)

api.add_resource(Search, '/search')

if __name__ == '__main__':
     app.run(port='5002')
