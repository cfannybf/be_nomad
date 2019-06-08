import urllib.request
import urllib.parse
from search.search_base import SearchBase
from search.stack_overflow_parser import StackOverflowParser

class StackOverflow(SearchBase):
    def __init__(self):
        SearchBase.__init__(self, 'stack_overflow')
        self.base_query = 'https://stackoverflow.com/jobs?r=true'
    
    def Search(self, filter):
        result = self.SendQuery(filter)
        retval = StackOverflowParser().ParseResult(result)
        return SearchBase.Search(self, retval)
    
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