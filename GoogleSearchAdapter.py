# TODO: craw the google results using a web crawler of your choice
# TODO: for every result obtain the title and source_url of the results together
# with the first 100characters of the article, if the result has media(photos, pdfs, etc)
# proceed to get the url of these media files
# TODO: use selenium or beautiful soup if possible

import requests

class GoogleSearch:
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm

    def getSearchInfo(self):
        response = requests.get(self.searchTerm).text
