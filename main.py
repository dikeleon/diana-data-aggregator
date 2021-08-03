import requests

class Diana:
    # TODO: TEST
    def __init__(self, name):
        self.name = name
        self.searchEngines = ['https://google.com',]

    def setName(self, name):
        self.name = name

    def setSearchEngine(self, searchEngine):
        self.searchEngines.append(searchEngine)

    def getSearchData(self, searchTerm):
        # return a list of results from different sources
        return [requests.get(str(search_engine)+'/search?q=%s'%searchTerm).text for search_engine in self.searchEngines]


assistant = Diana('Diana')
assistant.setSearchEngine('https://bing.com')
print(assistant.getSearchData('intellithornCash'))
