from search.search_base import SearchBase
from search.wework_parser import WeWorkParser

class WeWork(SearchBase):
    def __init__(self):
        SearchBase.__init__(self, 'wework', 'https://weworkremotely.com/remote-jobs/search')
    
    def Search(self, filter):
        result = self.SendQuery(self.BuildQuery(filter))
        retval = WeWorkParser().ParseResult(result)
        return SearchBase.Search(self, retval)
    
    def BuildQuery(self, filter):
        query = self.base_query
        token = '?'
        if filter.keywords:
            query = query + token + 'term={}'.format(filter.keywords[0])
            token = '&'
        return query
