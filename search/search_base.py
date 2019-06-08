class SearchBase:
    def __init__(self, name):
        self.name = name
    
    def Search(self, result):
        return {'source': self.name, 'result': result}
