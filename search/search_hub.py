from search.stack_overflow import *
from search.remoteok import *
from search.wework import *

class SearchHub:
    def __init__(self):
        self.search_nodes = {
            'stack_overflow': StackOverflow(),
            'remoteok': RemoteOk(),
            'wework': WeWork()
        }
    
    def Search(self, filter):
        result = []
        for key in self.search_nodes:
            if key not in filter.excluded:
                result.append(self.search_nodes[key].Search(filter))
        return result
