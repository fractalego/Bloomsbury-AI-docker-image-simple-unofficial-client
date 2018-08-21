import requests


class BloomsburyClient():
    
    def __init__(self, url):
        self._url = url + '/api/0.1/answer?token=demo'
        self._text = ''
        
    def text(self, doc):
        self._text = doc

    def ask(self, query):
        return requests.get(self._url
                         + '&question=' + query.replace(' ', '+')
                         + '&text=' + self._text.replace(' ', '+')                    
        ).json()['result']['items']


if __name__ == '__main__':
    client = BloomsburyClient('http://localhost:5050')
    client.text('This is a test')
    responses = client.ask('what is this?')
    for item in responses:
        print(item['answerText'])
