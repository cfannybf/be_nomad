import urllib.request
import urllib.parse
from urllib.request import Request

class SearchBase:
    def __init__(self, name, base_query):
        self.name = name
        self.base_query = base_query
    
    def Search(self, result):
        return {'source': self.name, 'result': result}
    
    def BuildQuery(self, filter):
        query = self.base_query
        if filter.keywords:
            query = query + '&q={}'.format(filter.keywords)
        if filter.min_salary > 0:
            query = query + '&s={}&c={}'.format(str(filter.min_salary), filter.currency)
        return query

    def SendQuery(self, query):
        f =  urllib.request.urlopen(Request(query, data=None, headers={
            'User-Agent': 'PostmanRuntime/7.13.0'
        }))
        return f.read().decode('utf-8')
