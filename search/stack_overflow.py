from search.search_base import SearchBase
from search.stack_overflow_parser import StackOverflowParser

class StackOverflow(SearchBase):
    def __init__(self):
        SearchBase.__init__(self, 'stack_overflow', 'https://stackoverflow.com/jobs?r=true')
    
    def Search(self, filter):
        result = self.SendQuery(self.BuildQuery(filter))
        retval = StackOverflowParser().ParseResult(result)
        return SearchBase.Search(self, retval)
