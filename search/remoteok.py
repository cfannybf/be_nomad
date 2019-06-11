from search.search_base import SearchBase
from search.remoteok_parser import RemoteOkParser

class RemoteOk(SearchBase):
    def __init__(self):
        SearchBase.__init__(self, 'remoteok', 'http://remoteok.io/api')
    
    def Search(self, filter):
        result = self.SendQuery(self.base_query)
        retval = RemoteOkParser().ParseResult(result, filter)
        return SearchBase.Search(self, retval)
