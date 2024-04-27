import requests

def request_get(url):
    return requests.get(url).json()



