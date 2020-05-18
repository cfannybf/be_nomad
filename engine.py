from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
from filter import Filter
from search.search_hub import SearchHub
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

class Search(Resource):
    def get(self):
        query = request.args
        filter = Filter()
        filter.ParseArgs(query)
        result = {'results': SearchHub().Search(filter)}
        return jsonify(result)

api.add_resource(Search, '/search')

if __name__ == '__main__':
     app.run(port='5002')
