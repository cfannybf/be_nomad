class Filter:
    def __init__(self):
        self.keywords = ''
        self.min_salary = 0
    
    def ParseToInt(self, txt):
        try:
            return int(txt)
        except ValueError:
            return 0
    
    def ParseArgs(self, query):
        if 'keywords' in query:
            self.keywords = query['keywords'].split(',')
        if 'min_salary' in query:
            self.min_salary = self.ParseToInt(query['min_salary'])
