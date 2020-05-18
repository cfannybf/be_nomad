import json
from datetime import datetime
import timeago

class RemoteOkParser:
    def __init__(self):
        pass
    
    def ParseResult(self, result, filter):
        structure = json.loads(result)
        result = self.FilterResult(structure, filter)
        return self.FormResult(result)
    
    def FilterResult(self, structure, filter):
        structure = structure[1:]
        result = []
        for item in structure:
            if filter.keywords:
                if all(tag in item['tags'] for tag in filter.keywords):
                    result.append(item)
        return result
    
    def FormResult(self, result):
        retval = []
        for item in result:
            date = datetime.strptime(item['date'][:10], '%Y-%m-%d')
            time = timeago.format(date, datetime.now())
            retval.append({
                'title': item['position'],
                'tags': item['tags'],
                'company': item['company'],
                'link': item['url'],
                'salary': '',
                'time': time
            })
        
        return retval
