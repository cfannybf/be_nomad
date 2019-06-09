import urllib.request
import urllib.parse
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

    def SendQuery(self, filter):
        f =  urllib.request.urlopen(self.BuildQuery(filter))
        return f.read().decode('utf-8')
